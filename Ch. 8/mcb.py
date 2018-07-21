#! /usr/bin/env python3
'''
mcb.py - Saves and loads pieces of text to the clipboard, tied to keywords for easy recall.

E.g.:   ./mcb.py save <keyword>     - saves clipboard contents to keyword
        ./mcb.py <keyword>          - loads associated keyword's contents to clipboard
        ./mcb.py list               - lists all currently saved keywords
        ./mcb.py delete <keyword>   - delete keyword from list
        ./mcb.py clear              - delete all keywords from shelf
'''

import shelve, pyperclip, sys

mcbshelf = shelve.open('mcb', 'c')

# Save clipboard content:

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    
    mcbshelf[sys.argv[2]] = pyperclip.paste()

# Add delete functionality:

if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    
    if sys.argv[2] in mcbshelf:
        del mcbshelf[sys.argv[2]]
    else:
        print('Key not in clipboard')
        
# List Keywords and load content:

elif len(sys.argv) == 2:
    
    if sys.argv[1].lower() == 'list':
        
        pyperclip.copy(str(list(mcbshelf.keys())))
        print(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])

    if sys.argv[1].lower() == 'clear':
        mcbshelf.clear()
        
mcbshelf.close()
