
def listToStr(list):
    str = ''
    for i in range(len(list)):
        if i < (len(list) - 2):
            str = str + list[i] + ','

        elif i == (len(list) - 2):
            str = str + 'and ' + list[len(list) - 1]
    return str

spam = ['apples', 'bananas', 'tofu', 'cats']

print(listToStr(spam))
