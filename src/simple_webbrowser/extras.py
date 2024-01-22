import webbrowser
from typing import Literal

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

def DoomWorld(query: str):
    Search("https://www.doomworld.com/search/?q=", query, "%20")

def DeepL(query: str, _lang: str = "en"):
    Search(f"https://www.deepl.com/translator#{_lang}/", query, "%20")

def Twitch(query: str):
    Search("https://www.twitch.tv/search?term=", query, "%20")
