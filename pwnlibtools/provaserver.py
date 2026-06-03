from pwn import *
import random

str_port=''.join(map(str, (random.randint(0,4) for i in range (0, 4))))
port=int(str_port)
myserver=server(port)
connection=myserver.
print(myserver.lport)


while True:
    data=myserver.recvline()
    print(data)

connection.close()
myserver.close()

