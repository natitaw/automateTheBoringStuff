#! python3
import re
'''
regex version of the string method strip()
'''




def regexStrip(string):
    stripRegex = re.compile(r'\s+')
    
    if stripRegex.search(string) == None:
        return string
    else:
        string = stripRegex.sub(r'', string)
    return string
        
