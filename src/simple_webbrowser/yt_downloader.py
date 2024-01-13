from pytube import YouTube, Playlist
from argparse import ArgumentParser, Namespace
from colorama import Fore as fg

# [*] Change 1: Update the timeout to a smaller one

# [!?] In case you have doubts, please use the '-h' flag.
# [!!] PLEASE NEVER USE THIS WITH MALICIOUS INTENTS
# [i] This was only made for educational purposes!

def clamp(value, _min, _max):
    if value > _max:
        return _max
    
    if value < _min:
        return _min
    
    return value

parser: ArgumentParser = ArgumentParser("YT Downloader by MF366", None, "Download YouTube videos or audios.")

def download_video(**kwargs):
    link: str = kwargs["link"]
    filename: str | None = kwargs["filename"]
    audio_only: bool = kwargs["audio_only"]
    vid_resolution: str = kwargs["resolution"]
    audio_subtype: str = kwargs["subtype"]
    sv_desc: bool = kwargs["save_description"]
    is_playlist: bool = kwargs["playlist"]
    extra_timeout: int = kwargs["extra_timeout"]
    
    ytStreams: YouTube | Playlist | None = None
    
    if is_playlist:
        ytStreams = Playlist(link)
        
    else:
        ytStreams = YouTube(link)
    
    if filename == None:
        filename = ""
    
    if not is_playlist:
        if ytStreams.age_restricted and filename == '':
            filename += "[18+]-"
            
        if filename in {'[18+]-', ''}:
            filename += f"{str(ytStreams.author)}-{str(ytStreams.title)}"
            filename = filename.replace(" ", "_")
            filename = filename.replace("|", "_")
            filename = filename.replace("\\", "_")
            filename = filename.replace("/", "_")
            filename = filename.replace("<", "_")
            filename = filename.replace(">", "_")
            filename = filename.replace(":", "_")
            filename = filename.replace("*", "_")
            filename = filename.replace("\"", "_")
            filename = filename.replace("?", "_")
            
        if sv_desc:
            try:
                with open(f"{filename}_DATA.wclassic", "w", encoding="utf-8") as df:
                    df.write(f"{str(ytStreams.author)} - {str(ytStreams.title)}\n\nDescription:\n{str(ytStreams.description)}\n\nThumbnail URL:\n{str(ytStreams.thumbnail_url)}")
                    df.close()
                    
            except Exception as e:
                print(f"{fg.RED}[X] An error has occurred while atempting to write the YouTube data to a new file!\n{fg.YELLOW}Remember that filenames cannot contain certain characters!\n{fg.RESET}{e}")
        
        if audio_only:
            youtubeDownload = ytStreams.streams.get_audio_only(audio_subtype)
            ytStreams.streams.get_audio_only()
            
            filename += '.mp3'
            
        else:
            if vid_resolution == "highest":
                youtubeDownload = ytStreams.streams.get_highest_resolution()
                
            else:
                youtubeDownload = ytStreams.streams.get_lowest_resolution()
                
            filename += ".mp4"
        
        try:
            youtubeDownload.download(filename=filename, timeout=int(ytStreams.length / 10) + clamp(extra_timeout, 0, ytStreams.length * 3))
            
        except Exception as e:
            print(f"{fg.RED}[X] An error has occurred!\n{fg.RESET}{e}")
        
        else:  
            print(f"{fg.GREEN}[*] The download has completed successfully.{fg.RESET}")
    
        return
    
    num: int = 1
    
    for video in ytStreams.videos:
        filename: str = ""
        
        if video.age_restricted:
            filename += "[18+]-"
            
        filename += f"{str(video.author)}-{str(video.title)}"
        filename = filename.replace(" ", "_")
        filename = filename.replace("|", "_")
        filename = filename.replace("\\", "_")
        filename = filename.replace("/", "_")
        filename = filename.replace("<", "")
        filename = filename.replace(">", "")
        filename = filename.replace(":", "_")
        filename = filename.replace("*", "")
        filename = filename.replace("\"", "_")
        filename = filename.replace("?", "")
            
        if sv_desc:
            try:
                with open(f"{filename}_DATA.wclassic", "w", encoding="utf-8") as df:
                    df.write(f"{str(video.title)} - {str(video.title)}\n\nDescription:\n{str(video.description)}\n\nThumbnail URL:\n{str(video.thumbnail_url)}")
                    df.close()
                    
            except Exception as e:
                print(f"{fg.RED}[X] An error has occurred while atempting to write the YouTube data to a new file!\n{fg.YELLOW}Remember that filenames cannot contain certain characters!\n{fg.RESET}{e}")
                
        if audio_only:
            youtubeDownload = video.streams.get_audio_only(audio_subtype)
            
            filename += '.mp3'
            
        else:
            if vid_resolution == "highest":
                youtubeDownload = video.streams.get_highest_resolution()
                
            else:
                youtubeDownload = video.streams.get_lowest_resolution()
                
            filename += ".mp4"
        
        try:
            youtubeDownload.download(filename=filename, timeout=int(ytStreams.length / 10) + clamp(extra_timeout, 0, ytStreams.length * 3))
            
        except Exception as e:
            print(f"{fg.RED}[X] An error has occurred while downloading video #{num}!\n{fg.RESET}{e}")
        
        else:
            print(f"{fg.GREEN}[*] The download of video #{num} has completed successfully.{fg.RESET}")

        num += 1

parser.add_argument("url", type=str, help="The link for the video to download.")
parser.add_argument("-f", "-n", "--filename", type=str, help="A custom filename. If none given, it will be chosen automatically. If downloading a playlist and this argument has been given a value, it will be ignored.", default=None)
parser.add_argument("-a", "--audio", action="store_true", help="Use this argument to indicate if only the audio should be saved.")
parser.add_argument("-r", "--resolution", type=str, help="A string (either 'highest' or 'lowest') which will be used when downloading a certain video resolution. Defaults to 'highest'.", default='highest')
parser.add_argument("--subtype", type=str, help="The subtype for an audio only download. Recommended and default is 'mp4', which means the audio will be extracted from the MP4 version of the video.", default='mp4')
parser.add_argument("-d", "--savedata", "-s", action="store_true", help="Use this argument to indicate that a file with the data (title, author, description, thumbnail URL) should be saved next to the video.")
parser.add_argument("-p", "--playlist", "-l", action="store_true", help="Use this argument to indicate that the link refers to a playlist. Right now, this script can't figure it out by itself.")
parser.add_argument("--timeout", type=int, help="An integer which represents the extra time (alongside the length of the video) the API should wait until it gives up on trying to download the video. Minimum allowed is 0. Maximum allowed is the lenght of the video times 3. Defaults to 5.", default=5)

args: Namespace = parser.parse_args()

download_video(link=args.url,
    filename=args.filename,
    audio_only=args.audio,
    resolution=args.resolution,
    subtype=args.subtype,
    save_description=args.savedata,
    playlist=args.playlist,
    extra_timeout=args.timeout
)
