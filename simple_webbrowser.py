import webbrowser
from sys import platform

# simple_webbrowser.py by MF366
# Based on built-in module: webbrowser
# Also uses the platform variable from sys module

def Website(url):
    if platform == "win32":
        webbrowser.open(url)
        # trust me: this part is not a total waste
    elif platform == "linux" or "darwin":
        webbrowser.open(url)
        
def Google(query):
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open('https://www.google.com/search?q='+typed)
                
def Bing(query):
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open('https://www.bing.com/search?q='+typed)
                
def Yahoo(query):
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://search.yahoo.com/search?p="+typed)
                
def DuckDuckGo(query):
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://duckduckgo.com/?q="+typed)
                
def YouTube(query):
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://www.youtube.com/results?search_query="+typed)
                
def Ecosia(query):
    for i in query:
        typed = query.replace(' ', '%20')
    webbrowser.open("https://www.ecosia.org/search?method=index&q="+typed)
        
def StackOverflow(query):
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://stackoverflow.com/search?q="+typed)
                
def SoundCloud(query):
    for i in query:
        typed = query.replace(' ', '%20')
    webbrowser.open("https://soundcloud.com/search?q="+typed)
                
def Archive(query):
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://archive.org/search?query="+typed)
                
def Qwant(query):
    for i in query:
        typed = query.replace(' ', '+')
    webbrowser.open("https://www.qwant.com/?q="+typed)
                
def SpotifyOnline(query):
    for i in query:
        typed = query.replace(' ', '%20')
    webbrowser.open("https://open.spotify.com/search/"+typed)