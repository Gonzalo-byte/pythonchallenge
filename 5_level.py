"""
Level 5

Honestly I saw the answer ih this level

My steps--
1- In the page source we find a text "peak hell sounds familiar"
2- I replace "pickle" in the path parameter. This is a module of python to serialize the objects.
3- In one cookie the key "info" says "you should have followed busynothing." and I return to previus page
4- I never see thee banner.p file, idiot.

"""

from fileinput import close
import requests, pickle

text = requests.get('http://www.pythonchallenge.com/pc/def/banner.p').text
with open('message_5_level', 'w') as f:
    f.write(text)
    f.close()

with open('message_5_level','rb') as f:
    text = pickle.load(f)
    f.close()
for line in text:
    renglon=[]
    for tup in line:
        renglon.append(tup[0]*tup[1])
        
    print(''.join(renglon))