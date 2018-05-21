#! python3

# chronology.py     - for all files with a given prefex (say spam) this program
# will fill in the gaps in numbering between filenames (spam001.txt, spam003.txt)
# (will result in spam001.txt, spam002.txt)


import re, os

# TODO: ask for a prefix and fill all the files in the given folder

#print('What is the prefix?')
#prefix = input()
prefix = 'spam' #str(prefix)
#print('Where is the file?')
source = 'C:\\chapter8\\Tickets' #input()
source = os.path.abspath(source)


fileRegex = re.compile('{}(\d+).txt'.format(prefix))

requestedFiles = []
fileIndex = []

for directory, subfolders, filenames in os.walk(source):

    for file in filenames:

        if fileRegex.search(file) == None:
            continue
        mo = fileRegex.search(file).group(1)
        fileIndex.append(fileRegex.search(file).group(1))
        requestedFiles.append( (int(mo.lstrip('0')), file, len(mo)) )

requestedFiles = sorted(requestedFiles)
print(requestedFiles)

for index in range(len(requestedFiles)):
    padding = requestedFiles[index][2]
    num = str(int(index) + 1) 
    padded_num = num.rjust(padding, '0')
    print(padded_num)
    #src = os.path.join(source, lst[index][1])
    #dst = os.path.join(source, seq.sub(r'\g<1>%s\g<3>' % padded_num, lst[index][1]))
    #shutil.move(src, dst)




















    
