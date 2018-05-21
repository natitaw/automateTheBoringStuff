#! python3

#StrongPassword detector
'''
Enter password
Regex to check if password is strong
    at least eight characters long
    at least one digit
Return true if password is strong else return false
'''

import re

print('Please enter your passowrd')

#TODO create strong password regex

password = input()

passwordRegex = re.compile(r'''(
    ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d$@$!%*?&]{8,}
)''', re.VERBOSE)

if passwordRegex.search(password):
    print('Good Password')
else:
    print('Pathetic')
