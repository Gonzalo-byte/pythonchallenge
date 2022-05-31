"""
Level 4

We need to create a scrapper to receive a query parameter and request to the entire url, and change manually the query parameter when the instructions return another answer
"""

import requests as r
import re

def run(nothing):
  for i in range(100):
    texto = r.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+nothing).text
    nothing = re.search(r'\d+', texto)
    nothing = nothing.group(0)
    if nothing:
      print(nothing)
    run(nothing)
if __name__ == '__main__':
    run('1234')