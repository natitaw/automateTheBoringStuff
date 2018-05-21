#! python3
# mapIt.py  - program will open Google Maps location for a given address
# command line or clipboard

import sys, webbrowser, pyperclip

if len(sys.argv) > 1:
    # Get address from cmd
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)
