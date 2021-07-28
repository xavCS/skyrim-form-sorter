import os, quitWhile
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'This is my web scraping script; Contact me at tharasher@gmail.com'}
#it's more convenient to be able to just import names from a file
fromFile = input("Search for forms using a text file of names or enter them into program? [F/W]").lower() #f for file and w for while approach
formIDs = []

if fromFile == 'f':
    filePath = input("specify text file path: ")
    
    with open(filePath,'r') as charactersFile:
        characters = charactersFile.read().split(',')
       #create a new plain text file with a more sorted fashion for sseedit comparisons 
        with open('sortedNames.txt','w+') as newFile:
            sorted(characters, key=str.lower) # doesn't quite sort fully alphabetically given the nature of eswiki syntax, does a decent enough job though
            for i in range(len(characters)):
                newFile.write(f'{characters[i]}\n')
            
else:
    characters = []
    while quitWhile.x == True:
        addCharacter = input("character name that you want to remove: ")
        characters.append(addCharacter)

        if characters[-1] == '':
            characters.remove('')
    


for item in range(len(characters)):
    source = requests.get(f'https://elderscrolls.fandom.com/wiki/{characters[item]}', headers=headers).text
    soup = BeautifulSoup(source,'lxml')
    baseIDspan = soup.find_all('span',style='font-size:12px;font-family: monospace, sans-serif; text-transform: uppercase;')
    baseID = baseIDspan[1].text
    formIDs.append(baseID)
    # print(formIDs) for when something goes wrong and i need a quick index

#basic functionality for dlc forms where 'xx' are the leading characters
#needs work for all round compatibility with all dlc
for i in range(len(formIDs)):
    if formIDs[i][0:2] == 'xx':
        print("match found")
        loadorder = formIDs[i].replace('xx','02')
        formIDs[i]=loadorder


go = input("proceed with deletion? [Y/N]").lower()
if go == 'y':
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

print("process complete, see text file for alphabetically sorted names to make deletion in SSEedit easier")
