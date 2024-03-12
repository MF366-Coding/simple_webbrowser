import simple_webbrowser as swb
import random

commons = [swb.ARCHIVE_ORG_COMMON,
           swb.BING_COMMON,
           swb.BRAVE_COMMON,
           swb.DOOMWORLD_COMMON,
           swb.DUCKDUCKGO_COMMON,
           swb.ECOSIA_COMMON,
           swb.GITHUB_COMMON,
           swb.GITLAB_COMMON,
           swb.GOOGLE_COMMON,
           swb.QWANT_COMMON,
           swb.YAHOO_COMMON,
           swb.TWITCH_COMMON,
           swb.STACKOVERFLOW_COMMON,
           swb.SPOTIFY_COMMON,
           swb.SOUNDCLOUD_COMMON,
           swb.YOUTUBE_COMMON]

given_input: str = input('Insert a link (starting with https://) or a search query: ')

url_or_query: swb.LinkString = swb.LinkString(given_input.rstrip(), swb.UTF8, safe=swb.SLASH) # [i] I only needed to introduce the link but I wanted to showoff the constants

if given_input.lstrip().startswith('https://'):
    swb.website(url_or_query.link, link_rule=swb.NORMAL)

else:
    swb.website(swb.build_search_url(random.choice(commons),
                        url_or_query,
                        swb.PLUS))
