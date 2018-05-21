#! python3

# emailer.py    - takes an email address from the command line then sends a pasted
# email to the recepient

import sys, pyperclip, bs4, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


print('What is your email address?')
email = 'mytestpython2@gmail.com' # input()
# print('What is the password?')
passW = 'python11642' #input()

# print('What is the subject of your email?')
subject = 'subject' # input()




if len(sys.argv) > 1 :
    print('Email is being sent')
    emailAddress = sys.argv[1]
else:
    print('Please enter email address and run again')

content = pyperclip.paste()

browser = webdriver.Firefox()

browser.get('https://gmail.com')

emailElem = browser.find_element_by_id("identifierId")

emailElem.send_keys(email)

nextElem = browser.find_element_by_id('identifierNext')
nextElem.click()

time.sleep(2)

passwordElem = browser.find_element_by_name("password")
passwordElem.send_keys(passW)

passNext = browser.find_element_by_id("passwordNext")
passNext.click()

time.sleep(1)

browser.get('https://mail.google.com//mail//u//0//#inbox?compose=new')

time.sleep(1)

sendTo = browser.find_element_by_class_name("vO")
sendTo.send_keys(emailAddress)
sendTo.send_keys(Keys.TAB)

subj = browser.find_element_by_name("subjectbox")
subj.send_keys(subject)

emailContent = browser.find_element_by_xpath('//div[@aria-label="Message Body"]')
emailContent.click()
emailContent.send_keys(content)

emailContent.send_keys(Keys.LEFT_CONTROL+Keys.ENTER)

time.sleep(1)
browser.close()

print('Dana')
