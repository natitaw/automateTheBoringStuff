#! python3

# clearUp.py    - python program that will clear up space
#                 by deleting files that are greater than given MB's 

import os, shutil, send2trash

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


def clearUp(folder):
    print('What is the size of the files you want to delete?\n Give size in MB')
    size = input()
    size = int(size) * 1000000
    print('size = ', size)
    print('This will delete all files greater than %s' %(size))

    folder = os.path.abspath(folder)

    

    for filename in os.listdir(folder):

        for folderName, subfolders, filenames in os.walk(filename):
            for filename in filenames:
                filename = os.path.join(folderName, filename)
                if os.path.getsize(filename) >= int(size):
                    print(filename)
                    print('Uncomment if you really want to delete')
                    #send2trash.send2trash(filename)
                    
                
    
    print('Dana')

clearUp('C:\\chapter8')
