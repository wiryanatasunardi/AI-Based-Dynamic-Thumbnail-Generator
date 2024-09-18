# AI-Based-Dynamic-Thumbnail-Generator

This project is a web application that will allow users to generate dynamic thumbnails (GIFs) from video files. This project is developed using libraries such as FastAPI, OpenCV, MoviePy, Pytubefix, and Tensorflow to extract keyframes from video and create dynamic thumbnails. 

## Project Features
- Automatically download the video when a user has already inserted the YouTube URL
- Extract keyframes from the video that has been downloaded
- Generate a GIF thumbnail from selected frames
- Support video upscaling to HD resolution before GIF generation

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

