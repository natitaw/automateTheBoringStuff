catNames = []

while True:
    print('Enter name of cat ' + str(len(catNames) + 1) + '(or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames += [name]

    print('The cat names are:')
    for name in catNames:
        print('   ' + name)
