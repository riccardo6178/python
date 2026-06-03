import socket
import sys
from random import randint
def main():
    #port=int(''.join(map(str, (randint(0,3) for i in range(0,3)))))
    port=8888
    addr=('localhost', port)
    print(port)
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    conn, remoteaddr = s.accept()
    print(f'Connessione ricevuta da:{remoteaddr}')
    

    print(f'Server listening in : {addr}')
    try:
        
        while True:
            data=conn.recv(1024)
            if not data:
                print('Client disconnected')
            print(data.decode())
            
        
    except KeyboardInterrupt:
        print('Uscendo dal server')

def port_gen():
    port=int(''.join(map(str, (randint(0,4) for i in range(0,3)))))

if __name__=='__main__':
    main()