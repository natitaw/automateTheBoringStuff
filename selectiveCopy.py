#! python3

# selectiveCopy.py  - walks through a folder tree and searches for files
# with a certain file extension (.pdf .jpg...)
# copies these files to a new folder

import os, re, shutil

def selectiveCopy(folder):
    print('What kind of file would you like to copy?')
    typeOfFile = input()
    print('Where would you like your files to be copied?')
    fileDestination = input()

    folder = os.path.abspath(folder)

    fileDestination = os.path.abspath(fileDestination)
    if not os.path.exists(fileDestination):
        os.makedirs(fileDestination)

    for foldername, subfolders, filenames in os.walk(folder):
        print('Looking for %s files' %(typeOfFile))

        for filename in filenames:
            if filename.endswith(typeOfFile):
                shutil.copy(os.path.join(foldername, filename), fileDestination)


selectiveCopy('C:\\chapter8')
