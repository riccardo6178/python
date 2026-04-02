#si puo usare l'EOF per richiedere sempre in input all uetnte delle stringhe in questo modo:
d=dict()
with open("inifile.ini", "r+") as file:

    f.close()

    a=""

    while a != EOF:
        a=input("Inserisci il testo: ")
        if a != "EOF":
            file.write(a)
