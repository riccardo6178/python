from pwn import *
import socket


port=int(input('Inserisci il numero di porta:'))
connection=remote('localhost',port)

try:
    while True:
        stringa=input()
    
        connection.sendline(stringa)
except KeyboardInterrupt:
    print('Connessione terminata')
