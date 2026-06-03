from pwnlib.tubes.ssh import *


s1=ssh_channel_interactive(user='bandit0', host='bandit.labs.overthewire.org', port=2220, password='bandit0')
spawndir=s1.run('cat readme')
output=spawndir.recvall(timeout=2)
print(output)

