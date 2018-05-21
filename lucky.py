#! python3
# lucky.py      - takes a search term from cmd and opens mutiple tabs with search
# results from Google


'''
    Read cmd line arguments from sys.argv
    Fetch the search results page with the requests module
    Find the links to each search result
    call webbrowser.open() function to open the new browser
'''

import sys, requests, webbrowser, bs4, pyperclip


# TODO: get the term from sys.argv
if len(sys.argv) > 1:
    print('Googling...')
    res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
    res.raise_for_status()
    
else:
    print('Googling...')
    res = requests.get('https://www.google.com/search?q=' + pyperclip.paste())

# TODO: Retrieve top search result links

soup = bs4.BeautifulSoup(res.text, 'html.parser')


linkElems = soup.select('.r a')


# TODO: open links

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    #href is part of HTML
    
