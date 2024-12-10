from downloader import download_video
from validator import is_valid_url

from downloader import download_video

def interface(default_folder):
    url = input("Enter the YouTube video URL: ")
    resolution = input("Enter the desired resolution (e.g., 720p): ")
    print(download_video(url, resolution, default_folder))

