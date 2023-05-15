
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
            clientsockets.remove(cs)
        msg = msg.replace(separatortoken, ": ")
        
        for client_socket in clientsockets:
            client_socket.send(msg.encode())

while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    clientsockets.add(client_socket)
    
    t = Thread(target=listenforclient, args=(client_socket,))

    t.daemon = True
    t.start()
    while True:
        print('[#] Menu\n[1] Kick User\n[2] Shut down server')
        option = input()
        if option == '1':
            print('[#]Select User:')
            for client_socket in clientsockets:
                print(client_socket)
            tokick = input('Enter IP:\n')
            print('[*] Kicking...')
            clientsockets.discard(tokick)
            print('[-]Sucess!')
        if option == '2':
            False

for cs in clientsockets:
    cs.close()
s.close()

