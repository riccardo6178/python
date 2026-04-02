import socket
condition=1
while condition:
    print("0 per uscire")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.89.238", 4444))
    messaggio=input()
    if messaggio != 0:
       convertito=messaggio.encode('utf-8')
    client.send(convertito)
    if messaggio=="0":
        client.close()

