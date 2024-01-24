import webbrowser
from typing import Literal, Callable, Any

# [i] simple_webbrowser.py by MF366
# [*] Based on built-in module: webbrowser

def Website(url: str, new: Literal[0, 1, 2] = 0, autoraise: bool = True, browser: webbrowser.BaseBrowser | Callable | Any = webbrowser) -> bool:        
    return browser.open(url, new, autoraise)

def BuildSearchURL(common: str, query: str, spacebar_rule: Literal["%20", "+"]) -> str:
    """
    BuildSearchURL allows you to set rules to search on any website

    Args:
        common (str): the part of the URL that never changes
        query (str): the search query
        spacebar_rule (either '%20' or '+'): the way the search engine handles SPACEBAR buy replacing it by something else (the value of this argument)
    """
    return f"{common}{query.replace(' ', spacebar_rule)}"

class utils:
    def __init__(self, browser = webbrowser) -> None:
        self.browser = browser
    
    def DoomWorld(self, query: str):
        Website(BuildSearchURL("https://www.doomworld.com/search/?q=", query, "%20"), browser=self.browser)

    def DeepL(self, query: str, _lang: str = "en"):
        Website(BuildSearchURL(f"https://www.deepl.com/translator#{_lang}/", query, "%20"), browser=self.browser)

    def Twitch(self, query: str):
        Website(BuildSearchURL("https://www.twitch.tv/search?term=", query, "%20"), browser=self.browser)

def get(_using : str | None = None) -> webbrowser.BaseBrowser:
    return webbrowser.get(_using)
    
def Google(query: str):
    Website(BuildSearchURL('https://www.google.com/search?q=', query, "+"))

def Brave(query: str):
    Website(BuildSearchURL('https://search.brave.com/search?q=', query, "+"))
                
def Bing(query: str):
    Website(BuildSearchURL('https://www.bing.com/search?q=', query, "+"))
                
def Yahoo(query: str):
    Website(BuildSearchURL("https://search.yahoo.com/search?p=", query, "+"))
                
def DuckDuckGo(query: str):
    Website(BuildSearchURL("https://duckduckgo.com/?q=", query, "+"))
                
def YouTube(query: str):
    Website(BuildSearchURL("https://www.youtube.com/results?search_query=", query, "+"))
                
def Ecosia(query: str):
    Website(BuildSearchURL("https://www.ecosia.org/search?method=index&q=", query, "%20"))
        
def StackOverflow(query: str):
    Website(BuildSearchURL("https://stackoverflow.com/search?q=", query, "+"))
                
def SoundCloud(query: str):
    Website(BuildSearchURL("https://soundcloud.com/search?q=", query, "%20"))
                
def Archive(query: str):
    Website(BuildSearchURL("https://archive.org/search?query=", query, "+"))
                
def Qwant(query: str):
    Website(BuildSearchURL("https://www.qwant.com/?q=", query, "+"))
                
def SpotifyOnline(query: str):
    Website(BuildSearchURL("https://open.spotify.com/search/", query, "%20"))
    
def GitLab(query: str):
    Website(BuildSearchURL("https://gitlab.com/search?search=", query, "%20"))
    
def GitHub(query: str):
    Website(BuildSearchURL("https://github.com/search?q=", query, "+"))
