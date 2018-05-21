from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('col-md-4 col-lg-3')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name')
