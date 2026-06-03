from pathlib import Path
import os

filepath='./file.txt'
bigwords=['ADJECTIVE', 'NOUN', 'VERB']

file=open(filepath, 'r+', encoding='UTF-8')
contenuto=file.read()
print(contenuto)
parole=contenuto.split()

for word in parole:
    clean_word=word.strip('. ')    
    if clean_word in bigwords:
        parole[parole.index(word)]=input(f'Enter a {clean_word}:\n')
    
final_text=" ".join(parole)
file.seek(0)
file.write(final_text)
file.close()
