from strutturaalbero import BST, Nodo
from ipaddress import ip_address
from random import randint, shuffle
from collections import deque
import time

def ipToInt(ip: str) -> int:
    return int(ip_address(ip))

def intToIp(n: int) -> str:
    return str(ip_address(n))

def crea_ip() -> str:
    return f'{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}'

def crea_pacchetto(ip_sorgente):
    return {
        "ip_sorgente": ip_sorgente,
        "ip_destinazione": f'{randint(1, 223)}.{randint(0, 255)}.{randint(0, 255)}.{randint(1, 254)}',
        "porta_sorgente": randint(1024, 65535),
        "porta_destinazione": randint(1, 1024),
        "protocollo": "TCP" if randint(0, 1) else "UDP",
        "dimensione": randint(64, 1500),
    }
blacklist_ip = [crea_ip() for _ in range(1000)]
blacklist_bst = BST()

for ip in blacklist_ip:
    blacklist_bst.insert(ipToInt(ip))

ip_dalla_blacklist = [blacklist_ip[randint(0, 999)] for _ in range(10)]
ip_nuovi = []

while len(ip_nuovi) < 10:
    nuovo = crea_ip()
    if nuovo not in blacklist_ip:
        ip_nuovi.append(nuovo)
tutti_ip = ip_dalla_blacklist + ip_nuovi
shuffle(tutti_ip)
queue_pacchetti = deque()

for ip in tutti_ip:
    pkt = crea_pacchetto(ip)
    queue_pacchetti.append(pkt)

print(f"{len(queue_pacchetti)} pacchetti in coda (10 blacklist + 10 nuovi, mescolati)\n")
bloccati = 0
permessi = 0

while queue_pacchetti:
    pkt = queue_pacchetti.popleft()
    ip_src = pkt["ip_sorgente"]
    if blacklist_bst.search(ipToInt(ip_src)):
        stato = "BLOCCATO"
        bloccati += 1
    else:
        stato = "PERMESSO"
        permessi += 1
    print(f"{bloccati + permessi:<3} {ip_src:<18} {pkt['protocollo']:<7} {pkt['dimensione']:<6} {stato}")
print("=" * 65)
print(f"\nRIEPILOGO FINALE")
print(f"  Pacchetti bloccati: {bloccati}")
print(f"  Pacchetti permessi: {permessi}")
print(f"  Totale processati:  {bloccati + permessi}")
print()
blacklist_interi = [ipToInt(ip) for ip in blacklist_ip]
ip_test = []
for _ in range(500):
    if randint(0, 1) == 0:
        ip_test.append(ipToInt(blacklist_ip[randint(0, 999)]))
    else:
        ip_test.append(ipToInt(crea_ip()))
start_bst = time.perf_counter()
for ip in ip_test:
    blacklist_bst.search(ip)
end_bst = time.perf_counter()
tempo_bst = end_bst - start_bst
start_lista = time.perf_counter()
for ip in ip_test:
    _ = ip in blacklist_interi
end_lista = time.perf_counter()
tempo_lista = end_lista - start_lista

print("BENCHMARK: 500 ricerche — BST vs Lista")

print(f"  BST:    {tempo_bst:.6f} secondi")
print(f"  Lista:  {tempo_lista:.6f} secondi")
if tempo_bst > 0 and tempo_lista > 0:
    rapporto = tempo_lista / tempo_bst
    if rapporto >= 1:
        print(f"\n  Il BST è {rapporto:.1f}x più veloce della lista!")
    else:
        print(f"\n  La lista è {1/rapporto:.1f}x più veloce del BST")
