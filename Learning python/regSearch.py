#! python3
# !regSearch.py - Программа ищет и выводит во всех файлах .txt регулярное выражение
# !regSearch.py - The program searches and displays a regular expression in all .txt files
import re
import os

# search for txt files in a folder and write to the list
# поиск txt файлов в папке и запись в список
fileFolder = ','.join(os.listdir('.\\temp'))
regFile = re.compile(r'.*.txt')
searchFile = regFile.search(fileFolder)
txtFile = searchFile.group().split(',')
# open all .txt files in the folder and transfer to the list
# открытие всех файлов .txt, находящихся в папке и передача в список
searchString = ''
for index in range(len(txtFile)):
    openFile = open('.\\temp\\%s' % txtFile[index])
    searchString += openFile.read()
searchString = searchString.split('.')

# regular string search
# поиск строк согласно регулярному выражению
constRegex = re.compile(input('Что ищите? '))
for word in range(len(searchString)):
    searchWord = constRegex.search(searchString[word])
    if searchWord != None:
        print(searchString[word])
