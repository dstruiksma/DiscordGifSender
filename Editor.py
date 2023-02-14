from moviepy.editor import *

class Editor:

    video_path = None
    start_time = None
    end_time = None

    def __init__(self, video_path, start_time, end_time):
        self.video_path = video_path
        self.start_time = start_time
        self.end_time = end_time

    def writeGif(self):
        clip = VideoFileClip(self.video_path)
        clip = clip.subclip(self.start_time, self.end_time).resize(0.5)
        clip.write_gif("test.gif", program='ffmpeg')

    def setVideoPath(self, video_path):
        self.video_path = video_path

    def setTime(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time