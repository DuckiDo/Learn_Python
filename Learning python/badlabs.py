#! python3
# badlabs.py - The program reads text files and the user can add their own text instead of headers
import re

# Opening a file and passing a string to a variable in a list view
File = open('.\\Work folder\\1.txt')
wordInFile = File.read().split()
File.close()

# Regular expression to search
fileRegex = re.compile(r'ADJECTIVE|NOUN|VERB')
# Search in a variable of regular expressions and replacement I agree with the results
for word in range(len(wordInFile)):
    regexFile = fileRegex.search(wordInFile[word])
    if regexFile != None:
        if regexFile.group() == 'ADJECTIVE':
            wordInFile[word] = fileRegex.sub(
                input('Enter an adjective: '), wordInFile[word])
        elif regexFile.group() == 'NOUN':
            wordInFile[word] = fileRegex.sub(
                input('Enter a noun: '), wordInFile[word])
        elif regexFile.group() == 'VERB':
            wordInFile[word] = fileRegex.sub(
                input('Enter the verb: '), wordInFile[word])
# Convert the resulting list to a string and write to a file
text = ' '.join(wordInFile)
print(text)
finishFile = open('.\\Work folder\\2.txt', 'w')
finishFile.write(text)
finishFile.close()
