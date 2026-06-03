from pwn import *
import socket

connection=remote('localhost',50007)

connection.sendline(b"Ciao questa e una stringa di prova")

