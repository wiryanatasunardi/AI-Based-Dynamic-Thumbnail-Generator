# AI-Based-Dynamic-Thumbnail-Generator

This project is a web application that will allow users to generate dynamic thumbnails (GIFs) from video files. This project is developed using libraries such as FastAPI, OpenCV, MoviePy, Pytubefix, and Tensorflow to extract keyframes from video and create dynamic thumbnails. 

## Project Features
- Automatically download the video when a user has already inserted the YouTube URL
- Extract keyframes from the video that has been downloaded
- Generate a GIF thumbnail from selected frames
- Support video upscaling to HD resolution before GIF generation

## Project Overview
The AI-based Dynamic Thumbnail Generator is a web-based application designed to generate animated GIF thumbnails from YouTube videos. By leveraging advanced deep learning techniques, the application automatically selects keyframes from a video to create a dynamic thumbnail that visually summarizes the content. This project streamlines the process of creating engaging video previews through the following workflow:

### 1. Video Downloading
Once a YouTube URL is provided, the video is downloaded in High Resolution (1080p) using the pytubefix library. The downloaded video is saved in the videos folder for further processing.

### 2. Keyframe Selection and Extraction
After the video is downloaded, it is broken down into individual frames. These frames are sampled based on the video's frame rate. The selected frames are then passed through a Convolutional Neural Network (CNN), specifically the VGG16 architecture, to extract the frame features. The CNN model identifies keyframes that are considered the most informative. These keyframes are then sorted according to their feature scores.

### Dynamic Thumbnail Generation
The top-ranked keyframes are then compiled to generate a dynamic thumbnail in the form of a GIF. This GIF represents a visual summary of the video, providing a quick and engaging preview. The generated thumbnail is displayed alongside the original video for comparison in the web interface

## Project Directory Tree

```bash
/project-directory/
├── Thumbnail_Video_Generator/
│   ├── static/
│   │   └── style.css        # CSS styling for the web interface
│   ├── templates/
│   │   └── index.html       # HTML layout for the web interface
│   ├── videos/              # Folder for storing downloaded videos
│   ├── thumbnails/          # Folder for storing generated GIFs
│   └── app.py               # FastAPI application backend
```
## Project Installation

1. Clone this repository:
   
	    git clone https://github.com/your-username/dynamic-thumbnail-generator.git

 2. Navigate into the project directory:
    
        cd project-directory

3. Install dependencies

       pip install -r requirements.txt

4. Run the FastAPI server through this command:
   
	    uvicorn Thumbnail_Video_Generator.app:app --reload

## How to Use

1. Open a browser and go to http://127.0.0.1:8000/.
2. Input a video URL from YouTube.
3. The web will process the video and generate an animated GIF thumbnail.
4. The generated GIF will be displayed in the preview section.

## Web Interface Preview
![UI Screenshot](https://github.com/wiryanatasunardi/AI-Based-Dynamic-Thumbnail-Generator/blob/main/Documentation/UI_Sample.png)

## Dynamic Thumbnail Preview
Dynamic Thumbnail
:-------------------------:
<img src="https://github.com/wiryanatasunardi/AI-Based-Dynamic-Thumbnail-Generator/blob/main/thumbnails/VENOM%20THE%20LAST%20DANCE%20%20%E2%80%93%20Final%20Trailer%20(HD).webm.gif" width="720" height = "480" /> <img src="https://github.com/wiryanatasunardi/AI-Based-Dynamic-Thumbnail-Generator/blob/main/thumbnails/Tate%20McRae%20-%20Greedy%20(Acoustic%20Session)%20NRJ.webm.gif" width="720" height = "480" />  

