from pytube import YouTube 
import ssl 
from tqdm import tqdm # for progression bar


ssl._create_default_https_context = ssl._create_unverified_context



url = input("Enter your youtube video URL : ")


video = YouTube(url)
video_stream = video.streams.get_highest_resolution()


with tqdm(total=video_stream.filesize) as pbar:
    video_stream.download(filename='video.mp4')
    pbar.update(video_stream.filesize)
