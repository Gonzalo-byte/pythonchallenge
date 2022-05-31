"""
Level 1.

We need to create a function to receive a letter and replace with letter +2 positions in the ascii numeration

after read the secret messagge, we need to pass the path parameter "map" in the function and the answer replace in path parameter
"""

import string

def run(message):
    letters = string.ascii_letters
    decrypt = [letters[letters.index(letter)+2] for letter in message if letter in letters]
    print(''.join(decrypt))

if __name__ == '__main__':
    message = input()
    run(message)