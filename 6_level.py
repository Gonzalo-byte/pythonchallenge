#www.pythonchallenge.com/pc/def/channel.zip
"""
Level 6
you need to create a function to read all zip files. after that you need to read the comments and print the answer
in the letters is the second secret

"""
from zipfile import ZipFile
import os
import re
import zipfile

comentarios = []
comentarios2 = []
def scrapper(archivo):

    directorio = str(os.path.dirname(__file__))
 
    try:
        with zipfile.ZipFile(directorio+'/channel'+'.zip','r') as f :
                comentarios.append(f.getinfo(archivo+'.txt').comment.decode())
                texto = f.read(archivo+'.txt').decode()
                match = re.search('\S[0-9]+',texto)
                match = match.group(0)
                print(match, " - ", texto)
        scrapper(match)
    except:
        print(''.join(comentarios))
        

if __name__ == '__main__':
    scrapper('90052')