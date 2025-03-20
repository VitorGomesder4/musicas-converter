from pytube import YouTube
import os

url = "YouTube video link"
yt = YouTube(url)
audio_stream = yt.streams.filter(only_audio=True).first()
audio_file = audio_stream.download(filename="audio.mp4")

# Convert to MP3
os.system("fffmspeg -i audio.mp4 -q:a 0 -map a audio.mp3")