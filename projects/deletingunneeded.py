from pathlib import Path
import os 

for folder, subfolders, filenames in os.walk(Path.home() / 'Documents'):
    for filename in filenames:
        file=os.path.join(folder, filename)
        filepath=Path(file)
        if filepath.stat().st_size*(1024**2)> 100:
            print(file)