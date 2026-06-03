import socket
import sys
import os

def main():
    
    try:
        hostname=sys.argv[1]
        print(socket.gethostbyname(hostname))
    except IndexError:
        print('''Usage: provasys.py 'host'
               ''')
    

   

if __name__=='__main__':
    main()
    