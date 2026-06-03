'''
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg). Copy these files from their cur-
rent location to a new folder.
'''

import os, shutil
from pathlib import Path
import sys


def selective_copy(folder, pattern, destination):
    files = []
    for folder_name, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.lower().endswith(pattern):
                source_path = Path(folder_name) / filename
                files.append(source_path)
    destination.mkdir(parents=True, exist_ok=True)
    for file in files:
        shutil.copy(file, destination)
    print(f"Copied {len(files)} file(s) to {destination}")

def main():
    if len(sys.argv)!=4:
        print("Usage: 'source' 'extension' 'destination'")
        sys.exit(1)
    else:
        folder=Path(sys.argv[1]).resolve()
        pattern=(sys.argv[2]).lower()
        destination=Path(sys.argv[3]).resolve()
        if not folder.is_dir():
            print('This is not a directory')
            sys.exit(1)
        
        selective_copy(folder, pattern, destination)

if __name__=='__main__':
    main()