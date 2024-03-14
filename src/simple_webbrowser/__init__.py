"""
Based on builtin module webbrowser, simple_webbrowser makes it way easier for you to search something online using Python.
"""

# [i] simple_webbrowser by MF366
# [*] Based on built-in module: webbrowser

# [i] Python imports
import webbrowser
from typing import Literal, Any, Iterable
from urllib import parse as parser

# [i] Constants for the developer's use

# [*] Encoding related
UTF8 = 'utf-8'
WINDOWS1252 = 'cp1252'
CP1252 = WINDOWS1252

# [*] Rule related
NORMAL = 'normal'
PLUS = 'plus'

# [*] Link parsing related
SLASH = '/'

# [*] Common search parts
GOOGLE_COMMON = 'https://www.google.com/search?q='
BING_COMMON = 'https://www.bing.com/search?q='
BRAVE_COMMON = 'https://search.brave.com/search?q='
YAHOO_COMMON = "https://search.yahoo.com/search?p="
DUCKDUCKGO_COMMON = "https://duckduckgo.com/?q="
YOUTUBE_COMMON = "https://www.youtube.com/results?search_query="
ECOSIA_COMMON = "https://www.ecosia.org/search?method=index&q="
STACKOVERFLOW_COMMON = "https://stackoverflow.com/search?q="
SOUNDCLOUD_COMMON = "https://soundcloud.com/search?q="
ARCHIVE_ORG_COMMON = "https://archive.org/search?query="
QWANT_COMMON = "https://www.qwant.com/?q="
SPOTIFY_COMMON = "https://open.spotify.com/search/"
GITLAB_COMMON = "https://gitlab.com/search?search="
GITHUB_COMMON = "https://github.com/search?q="
DOOMWORLD_COMMON = "https://www.doomworld.com/search/?q="
TWITCH_COMMON = "https://www.twitch.tv/search?term="


class LinkString:
    def __init__(self, url: str, encoding: str | None = 'utf-8', **kwargs: str | None | Iterable[int]) -> None:
        self._link: str = url
        self._encoding: str | None = encoding
        self._errors: str | None = kwargs.get('errors', None)
        self._safe: str | Iterable[int] = kwargs.get('safe', '/')
    
    def __repr__(self) -> str:
        return self._link
    
    @property
    def encoded_link(self) -> str:
        return parser.quote(self._link, self._safe, self._encoding, self._errors)
    
    @property
    def link(self) -> str:
        return self._link

    @property
    def encoded_link_plus(self) -> str:
        return parser.quote_plus(self._link, self._safe, self._encoding, self._errors)
    

class LinkBytes:
    def __init__(self, url: bytes | bytearray, safe: str | Iterable[int] = '/') -> None:
        self._link: str = url
        self._safe: str | Iterable[int] = safe

    def __repr__(self) -> str:
        return self.link
    
    @property
    def encoded_link(self) -> str:
        return parser.quote_from_bytes(self._link, self._safe)
    
    @property
    def link(self) -> bytes | bytearray:
        return self._link


def website(url: str | LinkString,
            new: Literal[0, 1, 2] = 0,
            autoraise: bool = True,
            browser: webbrowser.BaseBrowser | Any = webbrowser,
            **_) -> bool:
    """
    website opens a website using webbrowser

    Args:
        url (str | LinkString): a representation of an URL. If it's a LinkString, the original version of it will be considered the URL.
        new (Literal[0, 1, 2], optional): whether to use the current browser (default), a new window or a new browser page. Defaults to 0.
        autoraise (bool, optional): whether to focus the browser or not. Defaults to True.
        browser (webbrowser.BaseBrowser | webbrowser, optional): the browser class or module that will open the URL. Defaults to the webbrowser module (a.k.a.: webbrowser will use the default browser).
    
    Returns:
        bool: return value of the open operation
    """
    
    link = url
    
    if isinstance(url, LinkString):
        link = url.link

    return browser.open(link, new, autoraise)


def build_search_url(common: str,
                     query: str | LinkString | LinkBytes,
                     link_rule: Literal['normal', 'plus'] = 'normal') -> str:
    """
    build_search_url combines the common part of the URL and the parsed query into a search URL

    NOTE: the `common` argument is not parsed and must be a string, not LinkString nor LinkBytes!
    
    Args:
        common (str): the common search part. Examples: simple_webbrowser constants ending with COMMON.
        query (str | LinkString | LinkBytes): a representation of the already parsed URL. If it's a LinkString or a LinkBytes, the encoded version of it will be considered the URL.
        link_rule ('normal', 'plus'], optional): if using a LinkString as url and this is set to 'plus', use encoded_link_plus instead of encoded_link. When set to 'normal' or anything else really, use encoded_link. This argument is compatible with the NORMAL and PLUS constants. Defaults to 'normal'.

    Returns:
        str: the combined search URL
    """
    
    parsed_query = query
    
    if isinstance(query, LinkString):
        if link_rule == 'plus':
            parsed_query = query.encoded_link_plus
            
        else:
            parsed_query = query.encoded_link
            
    elif isinstance(query, LinkBytes):
        parsed_query = query.encoded_link
    
    return f"{common}{parsed_query}"


# [*] Variables for scripts that used the old variable names
Website = website
BuildSearchURL = build_search_url
get_browser_class = webbrowser.get
register_connector = webbrowser.register

# [*] Search engines
Google = lambda query: website(build_search_url(GOOGLE_COMMON, parser.quote(query, 'utf-8')))
Bing = lambda query: website(build_search_url(BING_COMMON, parser.quote(query, 'utf-8')))
Brave = lambda query: website(build_search_url(BRAVE_COMMON, parser.quote(query, 'utf-8')))
Yahoo = lambda query: website(build_search_url(YAHOO_COMMON, parser.quote(query, 'utf-8')))
DuckDuckGo = lambda query: website(build_search_url(DUCKDUCKGO_COMMON, parser.quote(query, 'utf-8')))
YouTube = lambda query: website(build_search_url(YOUTUBE_COMMON, parser.quote(query, 'utf-8')))
Ecosia = lambda query: website(build_search_url(ECOSIA_COMMON, parser.quote(query, 'utf-8')))
StackOverflow = lambda query: website(build_search_url(STACKOVERFLOW_COMMON, parser.quote(query, 'utf-8')))
SoundCloud = lambda query: website(build_search_url(SOUNDCLOUD_COMMON, parser.quote(query, 'utf-8')))
Archive = lambda query: website(build_search_url(ARCHIVE_ORG_COMMON, parser.quote(query, 'utf-8')))
Qwant = lambda query: website(build_search_url(QWANT_COMMON, parser.quote(query, 'utf-8')))
SpotifyOnline = lambda query: website(build_search_url(SPOTIFY_COMMON, parser.quote(query, 'utf-8')))
GitLab = lambda query: website(build_search_url(GITLAB_COMMON, parser.quote(query, 'utf-8')))
GitHub = lambda query: website(build_search_url(GITHUB_COMMON, parser.quote(query, 'utf-8')))
OpenSpotify = SpotifyOnline


class ExtraEngines:
    def __init__(self, browser = webbrowser) -> None:
        self._browser = browser
        
        self.DoomWorld = lambda query: website(build_search_url(DOOMWORLD_COMMON, parser.quote(query, 'utf-8')), browser=self._browser)
        self.Twitch = lambda query: website(build_search_url(TWITCH_COMMON, parser.quote(query, 'utf-8')), browser=self._browser)

    def DeepL(self, query: str, _lang: str = "en"):
        Website(BuildSearchURL(f"https://www.deepl.com/translator#{_lang}/", query, "%20"), browser=self.browser)
    
    @property
    def browser(self):
        return self._browser


extras = ExtraEngines()
