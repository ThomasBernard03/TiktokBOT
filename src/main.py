from pytube import YouTube 
import ssl 
from tqdm import tqdm # for progression bar
from moviepy.editor import VideoFileClip


ssl._create_default_https_context = ssl._create_unverified_context


def download_video(url):
    video = YouTube(url)
    video_stream = video.streams.get_highest_resolution()


    with tqdm(total=video_stream.filesize) as pbar:
        video_stream.download(filename='video.mp4')
        pbar.update(video_stream.filesize)


def split_video(duration):
    num_parts = int(video_duration / duration)


    for i in range(num_parts):
        start_time = i * duration
        end_time = (i + 1) * duration

        part = video.subclip(start_time, end_time)
        part.write_videofile(f"part{i+1}.mp4")


    if video_duration % duration != 0:
        start_time = num_parts * duration
        end_time = video_duration

        last_part = video.subclip(start_time, end_time)
        last_part.write_videofile(f"part{num_parts + 1}.mp4")



url = input("Enter your youtube video URL : ")
download_video(url)



video = VideoFileClip("video.mp4" )
video_duration = video.duration


value = float(input(f"Enter a durantion between 10s and {video_duration}s : "))
if value < 10 or value > video_duration:
    print("The value entered is invalid. Please enter a duration between 10s and the video duration.")
    exit()

split_video(value)








