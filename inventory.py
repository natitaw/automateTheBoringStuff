import pprint
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(dict):
    print('Inventory: ')
    total = 0
    for k,v in dict.items():
        pprint.pprint(str(v) + ' ' + str(k))
        total = total + v
    print('Total number of items is: ' + str(total))


#def addToInventory(dict, list):
#    for item in range(len(list) - 1):
#        if list[item] not in dict.keys():
#            dict[item] = 0
#        elif list[item] in dict.keys():
#            dict.keys(item) += 1
#    return dict

def addToInventory(dict, list):
    for item in list:
        dict.setdefault(item, 0)
        dict[item] += 1
    return dict


dict = {'gold coin': 42, 'rope': 1}
displayInventory(dict)
list = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'ruby']
inv = addToInventory(dict, list)
displayInventory(inv)
