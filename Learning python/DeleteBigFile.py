#! python3
# DeleteBigFile.py - The program finds and deletes files larger than number mb. Task from the book Automate the Boring Stuff with Python.
# github.com/DuckiDo/Learn_Python

import os

# Directory tree traversal
tree = os.walk(input('Enter an absolute directory path: '))
numberMB = input('Enter the file weight limit in MB: ')
for addres, folders, files in tree:
    for file in files:
        sizeFile = os.path.getsize(addres + os.path.sep + file) # file size by absolute path
        if sizeFile > (int(numberMB) * 1000000):
            print(addres + os.path.sep + file + '  delete')
            #os.unlink(addres + os.path.sep + file) # to delete a file
        else:
            continue