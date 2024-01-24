# simple_webbrowser
`simple_webbrowser` is a module that makes `webbrowser` module way more simple to work with.

**This module has been recently reestructurated with a new `__init__.py` file so you don't have to import `simple_webbrowser` from `simple_webbrowser`, which is pointless and deprecated after version 0.1.4.** Apps that used that are still compatible though!

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
import simple_webbrowser as swb

# Afterwards, you can use it :)
```

## A program that searches on Google
```py
# Just an example of what you can do with this module
# Not a great example though
import simple_webbrowser as swb

try:
	x = input()
	swb.Google(query=x)
except:
	swb.Google("empty :(")
```

# Projects where this module is used... (GitHub)
**Search query:** [simple_webbrowser language:Python](https://github.com/search?q=simple_webbrowser+language%3APython&type=code)

**Filters:** code
