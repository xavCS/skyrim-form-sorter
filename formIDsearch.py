import os, quitWhile
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'This is my web scraping script; Contact me at tharasher@gmail.com'}

characters = []

while quitWhile.x == True:
    addCharacter = input("character name that you want to remove: ")
    characters.append(addCharacter)

if characters[-1] == '':
    characters.remove('')

formIDs = []

for item in range(len(characters)):
    source = requests.get(f'https://elderscrolls.fandom.com/wiki/{characters[item]}', headers=headers).text
    soup = BeautifulSoup(source,'lxml')
    baseIDspan = soup.find_all('span',style='font-size:12px;font-family: monospace, sans-serif; text-transform: uppercase;')
    baseID = baseIDspan[1].text
    formIDs.append(baseID)
    

while True:
    path = input("enter path: ")
    os.chdir(path)
    
    
    extension = os.listdir()[0].split('.')[1]
    removeThese = [f'{formIDs[form]}.{extension}' for form in range(len(formIDs))]
    print(removeThese)
    for comparison in range(len(removeThese)):
        if removeThese[comparison] in os.listdir():
            os.remove(f'{removeThese[comparison]}')

    continue_ = input("need to delete these files from another directory? [Y/N]").lower()
    if continue_ != 'y':
        break
    