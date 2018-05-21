#! python3
# imageDownloaderImgur.py   - Downloads images by tag


import sys, requests, bs4, selenium, os,re
from bs4 import BeautifulSoup

# TODO prompt user to give a tag name

print('What would you like to download from Imgur.com today Sir?')
tag = input()

print('Downloading...')

path = 'C:\\chapter11'
url = 'http://imgur.com//search?q='
url += tag

realPath = path + '\\' + 'imgurimages\\' + tag
os.makedirs(realPath, exist_ok = True)

# os.makedirs(path + '\\' + tag, exist_ok = True)

res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")

imageLinks = []
imageLinksFixed = [] # contains URL of all images

for data in soup.find_all('div', {"id": "content"}):
        for getClass in soup.find_all('div', {"class":"cards"}):
            for getImg in getClass.find_all('a', {"class":"image-list-link"}):
                for getSrc in getImg.find_all('img', src = True):
                    imageLinks.append(getSrc['src'])

regUrl = re.compile('b.jpg')

for link in imageLinks:
    imageLinksFixed.append(regUrl.sub('.jpeg',link))


for link in imageLinksFixed:
    urlDown = 'http:' + link
    res = requests.get(urlDown)
    res.raise_for_status()
    # print(urlDown)
    imageFile = open(os.path.join(realPath, os.path.basename(urlDown)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    
print('Dana')
