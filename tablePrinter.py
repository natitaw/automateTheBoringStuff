

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]




def printable(listOfStrings):
    colWidth = []
    
    dict = {}
    for listOfWords in range(len(listOfStrings)):
        colWidth.append(len(max(tableData[listOfWords], key = len)))

    for x in range(len(listOfStrings[0])):
        for y in range(len(listOfStrings)):
            print(listOfStrings[y][x].rjust(colWidth[y]), end = ' ')
        print('')
#print(printable(tableData))
#printable(tableData)

#tableData[List][wordInList]




#print(tableData[2][0])
