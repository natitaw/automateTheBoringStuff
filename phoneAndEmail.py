#! python3

#phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

'''
#Get the text off the clipboard - pyperclip

#Find all phone numbers and emails from the text
    #one regex for phone numbers
    #one regex for emails
    #find all matches

#format text
#paste the found numbers and emails on the clipboard
#Display message if nothing is found
'''

import pyperclip, re

#TODO create phone regex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  #area code
    (\s|-|\.)?          #separator (space or dash or dot)
    (\d{3})             #first 3 digits
    (\s|-|\.)           #separator
    (\d{4})             #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
    )''', re.VERBOSE) #re.VERBOSE for complex regexes

#TODO create email regex

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+     #username
    @                     #@ symbol
    [a-zA-Z0-9.-]+        # domain name
    (\.[a-zA-Z]{2,4})     # dot-something
)''', re.VERBOSE)


#TODO Find matches and format

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0]) #group 0 matches entire reg expression

matches.sort()
#paste matches to clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipoard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')



