
from strutturaalbero import BST, Nodo
from ipaddress import ip_address
from random import randint
from collections import deque

ips=[]
pacchetti=[]

def ipToInt(ip):
    return int(ip_address(ip))

def intToIp(n):
    return str(ip_address(n))

def crea_ip():
    return f'{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}'
    
for i in range (1000):
    bstree=BST()
    ip=crea_ip()
    ip_int=ipToInt(ip)
    bstree.insert(ip)

blacklist_bst =  BST()





