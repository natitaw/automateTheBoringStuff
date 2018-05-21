grid = [['.', '.', '.', '.', '.', '.'],['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


def reformatGrid(listOfList):

    for list in range(0, len(listOfList[0])):

        str = ''

        for j in range(0, len(listOfList)):
            str += listOfList[j][list]
        print(str)

reformatGrid(grid)
    
            
