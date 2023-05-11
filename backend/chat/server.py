__name__ = 'chat'
import socket
from threading import Thread
from flask import Flask
app = Flask(__name__)

@app.route('/')
def start():
    print('starting...')
start()
serverhost = '127.0.0.1'
serverport = 3333
separatortoken = '<SEP>'
clientsockets = set()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((serverhost, serverport))
s.listen(5)
print(f"[*] Listening as {serverhost}:{serverport}")

def listenforclient(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        msg = msg.replace(separatortoken, ": ")
        
        for client_socket in client_sockets:
            client_socket.send(msg.encode())

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    clientsockets.add(client_socket)
    
    t = Thread(target=listenforclient, args=(client_socket,))

    t.daemon = True
    t.start()
for cs in client_sockets:
    cs.close()
s.close()

s = socket.socket()
print(f"[*] Connecting to {serverhost}:{serverport}...")

s.connect((serverhost, serverport))
print("[+] Connected.")
# gonna remake this soon
name = input("Enter your name: ")
def listenformessages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

t = Thread(target=listenformessages)
t.daemon = True

t.start()

while True:
    tosend = input()

    if to_send.lower() == 'q':
        break

    datenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{clientcolor}[{datenow}] {name}{separatortoken}{tosend}{Fore.RESET}"
    s.send(tosend.encode())
s.close()