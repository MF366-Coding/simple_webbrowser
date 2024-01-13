# simple_webbrowser
`simple_webbrowser` is a module that makes `webbrowser` module way more simple to work with.

## License
This module is licensed under the MIT License.

# Installing
Use the following command on the commandline:
```bash
pip install simple_webbrowser
```

Or, for Windows (if Python is on ``PATH``, but ``pip`` isn't):
```powershell
python -m pip install simple_webbrowser
```

# Usage
Import it like this:
```py
from simple_webbrowser import simple_webbrowser

# Afterwards, just use it :)
```

## A program that searches on Google
```py
# Just an example of what you can do with this module
from simple_webbrowser import simple_webbrowser as swb

try:
	x = input()
	swb.Google(query=x)
except:
	swb.Google("empty :(")
```

## YouTube Downloader
This project also comes with a YT Downloader that can be used as a script.

# Projects where this module is used... (GitHub)
Search query: [simple_webbrowser language:Python](https://github.com/search?q=simple_webbrowser+language%3APython&type=code)

Filters: code
