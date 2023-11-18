import requests


url = "https://parsinger.ru/video_downloads/videoplayback.mp4"

response = requests.get(url, stream=True)

with open("file.mp4", "wb") as video:

    for piece in response.iter_content(chunk_size=10000):
         video.write(piece)