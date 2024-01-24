from pytube import YouTube, Playlist
from colorama import Fore as fg
from typing import Literal, Any

# [!] PLEASE NEVER USE THIS WITH MALICIOUS INTENTS
# [i] This was only made for educational purposes!

__outputs: bool = True

def __print(*values: object, sep_end: tuple[str, None] = (" ", "\n"), file: Any = None, flush: Literal[False] = False) -> tuple[object] | None:
    if __outputs:
        return print(*values, sep=sep_end[0], end=sep_end[1], file=file, flush=flush)
        
    return values

def clamp(value, _min, _max):
    if value > _max:
        return _max
    
    if value < _min:
        return _min
    
    return value

def download_video(**kwargs):
    global __outputs
    
    link: str = kwargs["link"]
    filename: str | None = kwargs["filename"]
    audio_only: bool = kwargs["audio_only"]
    vid_resolution: str = kwargs["resolution"]
    audio_subtype: str = kwargs["subtype"]
    sv_desc: bool = kwargs["save_description"]
    is_playlist: bool = kwargs["playlist"]
    extra_timeout: int = kwargs["extra_timeout"]
    
    __outputs = kwargs["disable_output"]
    
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
                __print(f"{fg.RED}[X] An error has occurred while atempting to write the YouTube data to a new file!\n{fg.YELLOW}Remember that filenames cannot contain certain characters!\n{fg.RESET}{e}")
        
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
            __print(f"{fg.RED}[X] An error has occurred!\n{fg.RESET}{e}")
        
        else:  
            __print(f"{fg.GREEN}[*] The download has completed successfully.{fg.RESET}")
    
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
                __print(f"{fg.RED}[X] An error has occurred while atempting to write the YouTube data to a new file!\n{fg.YELLOW}Remember that filenames cannot contain certain characters!\n{fg.RESET}{e}")
                
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
            __print(f"{fg.RED}[X] An error has occurred while downloading video #{num}!\n{fg.RESET}{e}")
        
        else:
            __print(f"{fg.GREEN}[*] The download of video #{num} has completed successfully.{fg.RESET}")

        num += 1

def start_download(link: str, filename: str | None = None, audio_only: bool = False, resolution: Literal["lowest", "highest"] = 'highest', subtype: str = "mp4", save_description: bool = False, playlist: bool = False, extra_timeout: int = 5, autodetect_playlist: Literal["exact", "playlist", "list", "none"] = "exact", disable_output: bool = True):
    __MATCH = {
        "exact": "playlist?list=",
        "list": "list=",
        "playlist": "playlist?"
    }
    
    if autodetect_playlist != 'none' and __MATCH[autodetect_playlist] in link and not playlist:
        playlist = True
    
    download_video(link=link,
        filename=filename,
        audio_only=audio_only,
        resolution=resolution,
        subtype=subtype,
        save_description=save_description,
        playlist=playlist,
        extra_timeout=extra_timeout,
        output=disable_output
    )
