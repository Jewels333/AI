#this is the server that will be ran
import socket
from threading import Thread
from flask import Flask
app = Flask(__name__)

@app.route('/')
def start():
    print('starting...')
start()
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
serverhost = ip
serverport = 3333
separatortoken = '<SEP>'
clientsockets = set([])


s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((serverhost, serverport))
s.listen(5)
print(f"[*] Listening as {serverhost}:{serverport}")
#("""
def listenforclient(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            clientsockets.remove(cs)
        msg = msg.replace(separatortoken, ": ")
        clientsockets_copy = clientsockets
        for client_socket in clientsockets_copy:
            client_socket.send(msg.encode())

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    clientsockets.add(client_socket)
    
    t = Thread(target=listenforclient, args=(client_socket,))

    t.daemon = True
    t.start()
    
for cs in clientsockets:
    cs.close()
s.close()
#""")
#print(clientsockets)