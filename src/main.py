from pytube import YouTube 
import ssl 
from tqdm import tqdm # for progression bar
from moviepy.editor import VideoFileClip


ssl._create_default_https_context = ssl._create_unverified_context


url = input("Enter your youtube video URL : ")


video = YouTube(url)
video_stream = video.streams.get_highest_resolution()


with tqdm(total=video_stream.filesize) as pbar:
    video_stream.download(filename='video.mp4')
    pbar.update(video_stream.filesize)


video_path = "video.mp4"  
video = VideoFileClip(video_path)
video_duration = video.duration


value = float(input(f"Enter a durantion between 10s and {video_duration}s : "))
if value < 10 or value > video_duration:
    print("The value entered is invalid. Please enter a duration between 10s and the video duration.")
    exit()


num_parts = int(video_duration / value)


for i in range(num_parts):
    start_time = i * value
    end_time = (i + 1) * value

    part = video.subclip(start_time, end_time)
    part.write_videofile(f"part{i+1}.mp4")


if video_duration % value != 0:
    start_time = num_parts * value
    end_time = video_duration

    last_part = video.subclip(start_time, end_time)
    last_part.write_videofile(f"part{num_parts + 1}.mp4")