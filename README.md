# AI-Based-Dynamic-Thumbnail-Generator

This project is a web application that will allow users to generate dynamic thumbnail (GIFs) from video files. This project is developed using libraries such as FastAPI, OpenCV, MoviePy, Pytubefix, and Tensorflow to extract keyframes from video and create dynamic thumbnails. 

## Project Features
- Automatically download video when user has already inserted YouTube URL
- Extract keyframes from the video that has been downloaded
- Generate a GIF thumbnail from selected frames
- Support video upscaling to HD resolution before GIF generation

## Project Directory Tree

''' bash
/project-directory/
├── Thumbnail_Video_Generator/
│   ├── static/
│   │   └── style.css        # CSS styling for the web interface
│   ├── templates/
│   │   └── index.html       # HTML layout for the web interface
│   ├── videos/              # Folder for storing downloaded videos
│   ├── thumbnails/          # Folder for storing generated GIFs
│   └── app.py               # FastAPI application backend
'''

