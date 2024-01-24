# simple_webbrowser.py

# [!] Highly deprecated Python file
# [!?] Last update: 0.1.4
# [i] Instead you should take advantage on the existance of an __init__ file
# [*] Thank you for understanding!

from colorama import Fore, Back
import webbrowser

print(f"{Fore.RED}The use of '{Back.BLACK}{Fore.GREEN}from simple_webbrowser import simple_webbrowser{Fore.RED}{Back.RESET}' is not encouraged and the Python file only exists for compatibility reasons.{Fore.RESET}\nYou should do instead: '{Back.BLACK}{Fore.GREEN}import simple_webbrowser{Fore.RED}{Back.RESET}'.{Fore.RESET} Thank you")

def Website(url: str, new: int = 0, autoraise: bool = True) -> bool:        
    return webbrowser.open(url, new, autoraise)

def BuildSearchURL(common: str, query: str, spacebar_rule: str) -> str:
    """
    BuildSearchURL allows you to set rules to search on any website

    Args:
        common (str): the part of the URL that never changes
        query (str): the search query
        spacebar_rule (either '%20' or '+'): the way the search engine handles SPACEBAR buy replacing it by something else (the value of this argument)
    """
    return f"{common}{query.replace(' ', spacebar_rule)}"

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
