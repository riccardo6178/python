from pathlib import Path 
import os 
import random
path=Path.cwd()
home = Path.home()
documents = Path(f"{home}/Documents")
print(f"YOUR HOME: {Path.home()}")
print(f"YOUR DOCUMENT PATH {str(documents)}")

if Path.cwd()!= documents:
    print(f"Non e' la cartella documenti. sei in: {Path.cwd()}")
    os.chdir(documents)
    print(f"Ora sei in {Path.cwd()}")

    print(random.randint(3, 6))

frase="            Ciaooo questa e' una frase di prova          "

frase=frase.split('-')
print()