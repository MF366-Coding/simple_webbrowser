import webbrowser
from sys import platform

# simple_webbrowser.py by MF366
# Based on built-in module: webbrowser
# Also uses the platform variable from sys module

def Website(url: str, new: int = 0):
    if platform == "win32":
        webbrowser.open(url, new=new)
        # trust me: this part is not a total waste
    elif platform == "linux" or "darwin":
        webbrowser.open(url, new=new)
    else:
        raise OSError("Unidentified operating system.")
        
def Google(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open('https://www.google.com/search?q='+typed)

def Brave(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open('https://search.brave.com/search?q='+typed)
                
def Bing(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open('https://www.bing.com/search?q='+typed)
                
def Yahoo(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://search.yahoo.com/search?p="+typed)
                
def DuckDuckGo(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://duckduckgo.com/?q="+typed)
                
def YouTube(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://www.youtube.com/results?search_query="+typed)
                
def Ecosia(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '%20')
    webbrowser.open("https://www.ecosia.org/search?method=index&q="+typed)
        
def StackOverflow(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://stackoverflow.com/search?q="+typed)
                
def SoundCloud(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '%20')
    webbrowser.open("https://soundcloud.com/search?q="+typed)
                
def Archive(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://archive.org/search?query="+typed)
                
def Qwant(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://www.qwant.com/?q="+typed)
                
def SpotifyOnline(query):
    query = str(query)
    for i in query:
        typed = query.replace(' ', '%20')
    webbrowser.open("https://open.spotify.com/search/"+typed)
    
def GitLab(query):
    # requires a GitLab account
    query = str(query)
    for i in query:
        typed = query.replace(' ', '%20')
    webbrowser.open("https://gitlab.com/search?search="+typed)
    
def GitHub(query):
    # requires a GitHub account
    query = str(query)
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://github.com/search?q="+typed)
    
def func_namex(func) -> str:
    return f"{__name__}.{func.__name__}"

def pingx(func = Website, arg: str = "https://github.com") -> str:
    func(arg)
    return "Ping done!"
