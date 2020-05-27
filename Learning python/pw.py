#! python3
# pw.py - program for insecure password storage

import pyperclip
import sys
PASSWORDS = {'email': 'F209KDmcw',
             'blog': 'dlwpddowkdDwJDiajDIjwDhwuhd82uu98du',
             'luggage': '12345'}


if len(sys.argv) < 2:
    print('Use: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first arg command line - this is name users

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('Account ' + account + ' not listed.')
