from pytube import  YouTube, Stream
from pytube.cli import on_progress
import pytube as yt   
from pytube import Playlist 
import os


class yutube:

    def __init__(self) -> None:
        pass

    def download_video(self,url,folderDest,quality):
        try:   
            youtube = yt.YouTube(url)  
        
        except yt.RegexMatchError:
                return "Something Went Wrong  with video!"
        else:
            video = youtube.streams.filter(res=quality).first()
            file_size = video.filesize
            video.download(folderDest)  
            return "Downloaded Successfully"

    def donwload_highest_resolution(self, url, folderdir):
        try:
            youtube = yt.YouTube(url) 
            video = youtube.streams.get_highest_resolution()
            video.download(folderdir)  
            return "Downloaded Successfull!"
        except:
            youtube = yt.YouTube(url)  
            video = youtube.streams.filter(res="720p").first()
            video.download(folderdir)
            return "Error, downloaded in a low resolution" 

    def donwload_only_sound(self, url, dest):
        self.url = url
        self.dest = dest
        mp3 = '.mp3'

        try:
            youtube = yt.YouTube(url)  
            video = youtube.streams.filter(only_audio=True).first()
            file = video.download(dest)  
            base, ext = os.path.splitext(file)
            new_file = base + mp3
            os.rename(file,new_file)
            return "Download Successfull only sound"
        except:
            return "Something Went Wrong with sound!!"

    def download_playlist(self, url, dest):
        link = [url]
        urls = get_urls(link)
        count = 0
        print("urls",urls)
    
        for video in urls:
            try:
                youtube = yt.YouTube(video) 
                video = youtube.streams.get_highest_resolution()
                video.download(dest)  
                count +=1
                return "downloading video", count
            except:    
                return "Error in video ", count

def get_urls(self, playlists):
        urls = []
        for playlist in playlists:
            playlist_ruls = Playlist(playlist)
            for url in playlist_ruls:
                urls.append(url)
        return urls

#def progress_check(stream=None, chunk=None, file_handle=None, remaining=None):
#    val = (file_size - remaining) / file_size
    #print("val: " .format(val))
    