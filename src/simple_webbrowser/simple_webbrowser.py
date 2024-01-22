import webbrowser
from typing import Literal

# [i] simple_webbrowser.py by MF366
# [*] Based on built-in module: webbrowser

__chrome = webbrowser.Chrome()
__firefox = webbrowser.Mozilla()
__windefault = webbrowser.WindowsDefault()

def get(_using : str | None = None) -> webbrowser.BaseBrowser:
    return webbrowser.get(_using)

def Website(url: str, new: Literal[0, 1, 2] = 0, browser: Literal["mozilla", "chrome", "windows", "default"] = "default") -> bool:
    match browser:
        case "mozilla":
            return __firefox.open(url, new)
        
        case "chrome":
            return __chrome.open(url, new)
        
        case "windows":
            return __windefault.open(url, new)
    
    return webbrowser.open(url, new)

def Search(common: str, query: str, spacebar_rule: Literal["%20", "+"], new: Literal[0, 1, 2] = 0) -> bool:
    """
    Search allows you to set rules to search on any website

    Args:
        common (str): the part of the URL that never changes
        query (str): the search query
        spacebar_rule (either '%20' or '+'): the way the search engine handles SPACEBAR buy replacing it by something else (the value of this argument)

    If possible, open url in a location determined by `new`.
        - 0: the same browser window (the default).
        - 1: a new browser window.
        - 2: a new browser page ("tab"). If possible, autoraise raises the window (the default) or not.
    """
    
    return webbrowser.open(f"{common}{query.replace(' ', spacebar_rule)}", new=new)
    
def Google(query: str):
    Search('https://www.google.com/search?q=', query, "+")

def Brave(query: str):
    Search('https://search.brave.com/search?q=', query, "+")
                
def Bing(query: str):
    Search('https://www.bing.com/search?q=', query, "+")
                
def Yahoo(query: str):
    Search("https://search.yahoo.com/search?p=", query, "+")
                
def DuckDuckGo(query: str):
    Search("https://duckduckgo.com/?q=", query, "+")
                
def YouTube(query: str):
    Search("https://www.youtube.com/results?search_query=", query, "+")
                
def Ecosia(query: str):
    Search("https://www.ecosia.org/search?method=index&q=", query, "%20")
        
def StackOverflow(query: str):
    Search("https://stackoverflow.com/search?q=", query, "+")
                
def SoundCloud(query: str):
    Search("https://soundcloud.com/search?q=", query, "%20")
                
def Archive(query: str):
    Search("https://archive.org/search?query=", query, "+")
                
def Qwant(query: str):
    Search("https://www.qwant.com/?q=", query, "+")
                
def SpotifyOnline(query: str):
    Search("https://open.spotify.com/search/", query, "%20")
    
def GitLab(query: str):
    Search("https://gitlab.com/search?search=", query, "%20")
    
def GitHub(query: str):
    Search("https://github.com/search?q=", query, "+")
