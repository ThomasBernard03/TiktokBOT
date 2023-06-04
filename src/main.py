from pytube import YouTube


url = input("Enter your youtube video URL : ")


video = YouTube(url)


video_stream = video.streams.get_highest_resolution()
video_stream.download()
