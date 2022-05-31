"""
Level 3

Find the message in the page source and match the words with the pattern in the picture
"""
import re

def run():
    with open('./message_3_level.txt', 'r') as f:
        message = f.read()
        decrypt = re.findall('([a-z]{1})([A-Z]{3})([a-z]{1})([A-Z]{3})([a-z]{1})',message)
        final_message = [i[2] for i in decrypt]
        print(''.join(final_message))
if __name__ == '__main__':
    run()