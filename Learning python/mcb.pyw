#! python3
#mcb.pyw - saves and downloads text fragments to the clipboard.
# Usage:    py.exe mcb.pyw save <keyword> - Saves the clipboard to the keyword.
#           py.exe mcb.pyw <keyword> - Loads the keyword into the clipboard.
#           py.exe mcb.pyw list - Uploads all keywords to the clipboard.

import shelve, pyperclip, sys 

mcbShelve = shelve.open('mcb')
# save clipboard contents
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelve[sys.argv[2]]
elif len(sys.argv) == 2:
    # create a list of keywords and upload content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelve.keys())))
    elif sys.argv[1] in mcbShelve:
        pyperclip.copy(mcbShelve[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcbShelve.clear()
mcbShelve.close()