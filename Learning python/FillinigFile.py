#! python3
# Заполнение пропусков в нумерации файлов # Filling in File Numbering Gaps
# github.com/DuckiDo/Learn_Python
import re
import os
import shutil
# Регулярное выражение для поиска файлов с префиксами # Regular expression for finding files with prefixes
regexSearch = re.compile(r'(\D*)?(0*)?(\d+)(.*)', re.IGNORECASE)
prefixFile = []
# список для цифр перед префиксом (00 или 0 или без) # list for numbers before the prefix (00 or 0 or without)
numberOne = [] 
patchCatalog = input('Enter an absolute directory path: ')
os.chdir(patchCatalog)
# Обход дерева файлов # File tree traversal
tree = os.walk(patchCatalog)
for address, folders, files in tree:
    # Проход файлов по индексу # Pass files by index
    for i in range(len(files)):
        if regexSearch.match(files[i]) != None:
            # Разбиваем на группы # Break into groups
            searchFile = regexSearch.search(files[i])
            textNameFile = searchFile.group(1)
            # что бы у всех файлов был одинаковый префикс # so that all files have the same prefix
            numberOne.append(searchFile.group(2))
            numberMain = searchFile.group(3)
            # Добавляем в список prefixFile главное число # Add the main number to the prefixFile list.
            prefixFile.append(numberMain)
            expansionNameFile = searchFile.group(4)
            # Обноружение пропусков в нумерации # Identification of gaps in numbering
            if (int(prefixFile[i]) - int(prefixFile[i-1])) > 1:
                prefixFile[i] = int(prefixFile[i-1]) + 1
                # Изменение имена файла с следующим номером # Change file names with the following number
                shutil.move(address + os.path.sep + files[i], textNameFile + numberOne[0] + str(prefixFile[i]) + expansionNameFile)