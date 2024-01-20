from moviepy.editor import *
from tiktokvoice import *

import os
import random

def create_video(script, voice):
    background_video = VideoFileClip("background_video.mp4")

    tts(script, voice, "tts.mp3")
    tts_audio = AudioFileClip("tts.mp3")
    print("")

    start_time = random.randint(10, 1200)
    end_time = start_time + AudioFileClip("tts.mp3").duration + 2
    
    video = background_video.subclip(start_time, end_time)
    video = video.set_audio(tts_audio)

    original_width, original_height = video.size
    new_width = int(original_height * 9 / 16)

    crop_x1 = (original_width - new_width) // 2
    crop_x2 = original_width - crop_x1

    video = video.crop(x1=crop_x1, y1=0, x2=crop_x2, y2=original_height)

    credit = TextClip(".or104", color="white", fontsize=100, font="Calibri-Bold", stroke_color="black", stroke_width=3)
    credit = credit.set_position(("center", original_height - 200)).set_duration(video.duration)

    video = CompositeVideoClip([video, credit])

    video.write_videofile("video.mp4", codec="libx264", audio_codec="aac", bitrate="20000k", preset="slow", fps=60)


    os.remove("tts.mp3")