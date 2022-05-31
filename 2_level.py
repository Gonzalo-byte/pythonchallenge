"""
search in the page source the entire message to decript and replace the word in path parameter
"""

import string

def run():
    letters = string.ascii_lowercase
    with open('./message_2_level.txt', 'r') as f:
        message = f.read()
        decrypt = [letter for letter in message if letter in letters]
        print(''.join(decrypt))

if __name__ == '__main__':
    run()