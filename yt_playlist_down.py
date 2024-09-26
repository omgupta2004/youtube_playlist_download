from pytube import Playlist
pyt=input("enter the url of the playlist")
py= Playlist(pyt)

print(f'Downloading : {py.title}')

for video in py.videos:
   video.streams.first().download()