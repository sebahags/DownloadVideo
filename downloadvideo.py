from pytube import YouTube
#Downloads the youtube-video in the highest possible resolution in the directory of the script
url = r"url-path of the video"
the_video = YouTube(url)
the_video = the_video.streams.get_highest_resolution()
the_video.download()