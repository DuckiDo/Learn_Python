import os
import shutil
import re
# Regular expression to search for specific files
regexSearch = re.compile(r'.*\.docx')
# Traversing the directory tree and searching for files by reg expression
tree = os.walk('D:\\Work folder\\temp')
for address, dirs, files in tree:
    for file in files:
        absPathAllfile = address + '\\' + file
        if regexSearch.match(absPathAllfile) != None:
            # Copy selected files to a new folder
            shutil.copy(absPathAllfile, 'D:\\Work folder\\temp\\111')
