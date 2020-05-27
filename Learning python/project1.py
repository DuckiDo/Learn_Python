import re
import pyperclip
# Find phone number and email

phoneNumberRegex = re.compile(r'''(
                            (\+[7]|\s[8])?         #Russian cod mobile operator
                            (\s|-|\.)?           #Разделитель
                            (\d{3})                #Первые 3 цифры
                            (\s|-|\.)?           #Разделитель
                            (\d{3})
                            (\s|-|\.)?           #Разделитель
                            (\d{2})
                            (\s|-|\.)?           #Разделитель
                            (\d{2})
                                    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
                         \w*
                         @
                         \w*.\w*
                             )''', re.VERBOSE | re.IGNORECASE)

text = str(pyperclip.paste())

mathes = []

for groups in phoneNumberRegex.findall(text):
    phoneNumber = ' '.join(
        [groups[1], groups[3], groups[5], groups[7], groups[9]])
    mathes.append(phoneNumber)

for groups in emailRegex.findall(text):
    mathes.append(groups)

# Copy results to the clipboard.
if len(mathes) > 0:
    pyperclip.copy('\n'.join(mathes))
    print('Copied to clipboard:')
    print('\n'.join(mathes))
else:
    print('No phone numbers or email addresses found.')

