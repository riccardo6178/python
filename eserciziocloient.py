import socket 

def main():
    try:
        port=7777
        localaddr=('localhost', port)
        remote_addr=('localhost', 8888)
        addr=('localhost', port)
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(localaddr)
        s.connect(remote_addr)
        print(f'Connesso a {remote_addr}')
        while True:
            message=input()
            s.send(message.encode())
    except KeyboardInterrupt:
        print('Uscendo dal server')

if __name__=='__main__':
    main()