import socket 

s = socket.socket(socket.AF_ALG, socket.SOCK_SEQPACKET, 0)
s.bind(("hash", "sha256"))

h, _ = s.accept()
h.send(b'ciao')
digest = h.recv(32)

print(digest.hex())
