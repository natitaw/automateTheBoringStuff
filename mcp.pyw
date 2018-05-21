#! python3
# mcp.pyw - Saves and loads pieces of text to the clipboard

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - Loads all keywords to clipboard


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')


# TODO: Save clipboard content

    #sys.argv[1] - command line argument 1

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] == pyperclip.paste() #sys.argv[2] is used as a keyword
elif len(sys.argv) == 3 and sys.argv[1] == 'delete':
    if sys.argv[2] in mcbShelf:
        mcbShelf.pop(sys.argv[2])
    
elif len(sys.argv) == 2:
    # TODO: List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

elif len(sys.argv) == 4 and sys.argv[1] == 'delete all':
    mcbShelf.clear()
        

mcbShelf.close()
