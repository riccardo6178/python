
def append_key(key, value):
    ini_file='./ini-file.ini'
    with open(ini_file, 'a+') as inifile:
        inifile.write(f"{key}={value}")

def menu():
    while True:
        print('MENU')
        print('''
            0) per uscire  
            1) Per aggiungere una key
              ''')
        scelta=int(input('Scegli cosa fare: '))
        if scelta == 1:
            key=input('Inserisci un nome: ')
            value=input('Inserisci un voto: ')
            append_key(key, value)
        else:
            break

if __name__=='__main__':
    menu()