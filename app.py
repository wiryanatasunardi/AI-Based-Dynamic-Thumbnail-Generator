# Import Library

from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications import VGG16
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from fastapi import FastAPI, Request
from moviepy.editor import *
from pytubefix.cli import on_progress
from pytubefix import YouTube
import pytube
import numpy as np
import aiohttp
import cv2 
import os

# Load The Pre-Trained CNN Model with VGG16 Architecture
model = VGG16(weights='imagenet', include_top=False)

# Function to Download Video from YouTube URL
def download_video(video_url: str, output_path: str) -> str:
    try:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        print(yt.title)
        # stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        stream = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first()
        # stream = yt.streams.get_by_itag(137)

        # stream = yt.streams.get_highest_resolution()

        if stream is None:
            raise Exception("No valid stream found for this video.")

        os.makedirs(output_path, exist_ok=True)  # Ensure the directory exists
        file_path = stream.download(output_path=output_path)
        return file_path

    except pytube.exceptions.VideoUnavailable:
        raise Exception("The video is unavailable.")
    except pytube.exceptions.RegexMatchError:
        raise Exception("Invalid video URL.")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

# Function to Extract Keyframes from Video
def extract_keyframes_from_video(video_path: str, frame_rate: int = 1) -> list:
    """
    Extract frames from video at a specific frame rate (frames per second)
    """
    if not os.path.exists(video_path):
        print("Video path is incorrect or file does not exist.")
        
    cap = cv2.VideoCapture(video_path)
    frame_list = []
    fps = cap.get(cv2.CAP_PROP_FPS)  # Video FPS
    success, frame = cap.read()
    count = 0
    while success:
        # Select frames based on frame rate
        if count % int(fps / frame_rate) == 0:
            frame_list.append(frame)
        success, frame = cap.read()
        count += 1
    cap.release()
    return frame_list

# Function to Preprocess Frame
def preprocess_frame(frame):
    """
    Preprocess the frame to feed into the CNN model.
    Resizing the frame and converting it to a batch of size 1.
    """
    frame_resized = cv2.resize(frame, (224, 224))  # Resizing to 224x224 for VGG16
    frame_array = np.expand_dims(frame_resized, axis=0)
    return preprocess_input(frame_array)

# Applied AI Model to Extract Features and Identify Frames That are Informative
def extract_features(frames):
    """
    Use CNN to extract features for all frames.
    """
    features = []
    for frame in frames:
        frame_preprocessed = preprocess_frame(frame)
        feature = model.predict(frame_preprocessed)
        features.append(np.mean(feature))  # Mean of Extracted Features (Simplified Selection Criterion)
    return features

# Function to Select Keyframes
def select_keyframes(frames, features, num_keyframes=15):
    """
    Select keyframes based on the highest-scoring features.
    """
    # Select Top N keyframes
    keyframe_indices = np.argsort(features)[-num_keyframes:]  
    keyframes = [frames[i] for i in sorted(keyframe_indices)]
    return keyframes

# Function to Generate GIF as Thumbnail
def create_gif_from_keyframes(frames: list, output_gif: str) -> None:
    """
    Generate a GIF from selected keyframes.
    """
    clip = ImageSequenceClip([cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) for frame in frames], fps=5)  # Adjust the FPS
    clip.write_gif(output_gif, fps=5)

app = FastAPI()

# Mount to Static Directory Folder to Serve CSS File
app.mount("/static", StaticFiles(directory="Thumbnail_Video_Generator/static"), name="static")
app.mount("/thumbnails", StaticFiles(directory="Thumbnail_Video_Generator/thumbnails"), name="thumbnails")
app.mount("/videos", StaticFiles(directory="Thumbnail_Video_Generator/videos"), name="videos")


@app.get("/")
async def main_page():
    with open("Thumbnail_Video_Generator/templates/index.html") as f:
        return HTMLResponse(content=f.read())

@app.post("/generate-thumbnail/")
async def generate_thumbnail(request: Request):
    data = await request.json()
    video_url = data.get('video_url')
    
    if not video_url:
        return {"error": "Video URL not provided"}

    # Download Video from Youtube URL
    video_path = download_video(video_url, './Thumbnail_Video_Generator/videos')
    video_filename = os.path.basename(video_path)

    # Extract Keyframes from Downloaded Video
    frames = extract_keyframes_from_video(video_path, frame_rate=1)
    print(f"Number of frames extracted: {len(frames)}")

    features = extract_features(frames)
    print(f"Number of features extracted: {len(features)}")

    keyframes = select_keyframes(frames, features, num_keyframes=30)
    print(f"Number of keyframes selected: {len(keyframes)}")

    # Create GIF Keyframes
    gif_path = f"./Thumbnail_Video_Generator/thumbnails/{os.path.basename(video_path)}.gif"
    create_gif_from_keyframes(keyframes, gif_path)

    print(FileResponse(gif_path, media_type="image/gif"))

    gif_url = f"/thumbnails/{os.path.basename(gif_path)}"

    print(gif_url)

    # Return The GIF as Response
    return {"gif_url": gif_url, "video_filename": video_filename}
