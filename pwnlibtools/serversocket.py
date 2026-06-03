import socket
from random import randint 
str_port=''.join(map(str, (randint(0,4) for i in range (0,4))))
port=int(str_port)
addr=('',port)

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn=sock.bind(addr)
print(f'socket connected at {addr}')

sock.listen(5)

try:
    while True:
        print('\nIn attesa di un client')
        client, addr=sock.accept()
        print(f'Client connesso: {client}{addr}')
        while True:
            try:
                data=sock.recv(4096)
                if not data:
                    print(f'{client} Disconnesso')
                    break
                print(f'{addr}|{data.decode().strip()}')
                
            except ConnectionResetError:
                print(f'Client crashato')
                break
            client.close()
 
except KeyboardInterrupt:
    print("\n[*] Server fermato da tastiera")
finally:
    sock.close()


