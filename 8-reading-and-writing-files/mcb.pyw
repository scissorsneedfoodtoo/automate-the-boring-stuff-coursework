#!/usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: mcb.pyw save <keyword> - Saves clipboard to keyword
#        mcb.pyw del <keyword> - Deletes keyword's clipboard'
#        mcb.pyw <keyword> - Loads keyword to clipboard
#        mcb.pyw list - Loads all keywords to clipboard
#        mcb.pyw delall - Deletes all saved clipboards
#        mcb.pyw help - Display usage guide

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste() # keyword used as key for mcbShelf and the value will be the text currently on the clipboard

# Delete clipboard content
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]

# Only one command line argument and it's not save or del
elif len(sys.argv) == 2:
    # List all keywords
    if sys.argv[1].lower() == 'list':
        listOfKeys = str(list(mcbShelf.keys()))
        print(listOfKeys)
        pyperclip.copy(listOfKeys) # if the arg is list, copy list of keys from mcbShelf so user can paste to open text editor, and print to console

    # Delete all keywords and clipboard data
    elif sys.argv[1].lower() == 'delall':
        mcbShelf.clear()

    # display usage guide
    elif sys.argv[1].lower() == 'help':
        print()
        print('Usage:\n')
        print('mcb.pyw save <keyword> - Saves clipboard to keyword')
        print('mcb.pyw del <keyword> - Deletes keyword\'s clipboard')
        print('mcb.pyw <keyword> - Loads keyword to clipboard')
        print('mcb.pyw list - Loads all keywords to clipboard')
        print('mcb.pyw delall - Deletes all saved clipboards')

    # Load keyword's clipboard
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]]) # check if the keyword exists in mcbShelf and if so, load the value of the key to the clipboard

mcbShelf.close()
