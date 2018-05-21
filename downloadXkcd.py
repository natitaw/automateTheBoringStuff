#! python3
# downloadXckd.py   - downloads all images (on each page) by clicking on 'prev' from
#                     xkcd.com


'''
    Download pages with requests module
    Find the URL of comic image for page using Beautiful Soup
    Download and save image to hard drive with iter_content()
    Find the URL of the previous compic link and repeat
'''

import requests, os, bs4


os.chdir('C:\\chapter11') 
url = 'http://xkcd.com'

            
os.makedirs('xkcd', exist_ok = True) # store comics in ./skcd


while not url.endswith('#'):
    # TODO: Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")


    # TODO: Find the URL of the comic image
    comicElem = soup.select('#comic img') # id = comic , <img>
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')

    # TODO: Download the image
        print('Downloading image %s...' %(comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()


    # TODO: Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


    # TODO: Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


print('Dana')
