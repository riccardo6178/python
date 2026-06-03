import zipfile, sys, os
from pathlib import Path

def backup_zip(folder):
    folder=Path(folder)
    backup_zip=zipfile.ZipFile('backup.zip', 'w')

def iterdir(folder):
    for folder_name, subfolders, filenames in os.walk(Path(folder)):
        for file in filenames:
            zipup.write(folder_name / file)
    zipup.close()


def main():    
    if (len(sys.argv)) != 2:
        print("Usage: '/file/to/zip' ")
    
#TODO: Aggiungere capabilita' di fare zip di piu' cartelle

