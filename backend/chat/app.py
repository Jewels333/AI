#this is the server that will be ran
import socket
import sqlite3
import os
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
        clientsockets_copy = clientsockets.copy()
        
        for client_socket in clientsockets_copy:
            client_socket.send(msg.encode())
        
        if msg.startswith('script ') and admin == 1:
        #if tosend starts with 'script' and user is admin:
            if msg == 'script menu':
                adminMenu = {}
                adminMenu['1'] = 'Users'
                adminMenu['2'] = 'Server'
                adminMenu['3'] = 'Exit'
                while True:
                    options = adminMenu.keys()
                    for entry in options:
                        print(entry, adminMenu[entry])
                    selection = input('Select:')
                    if selection == '1':
                       print()
                       False
                       break
                    elif selection == '3':
                        False
                        break

while True:
    client_socket, client_address = s.accept()
    print(f"[...] {client_address} connecting")
    username = s.recv(1024)
    password = s.recv(1024)
    conn = sqlite3.connect('backend/chat/accounts.db')
    crsr = conn.cursor()
    crsr.execute('SELECT username FROM accounts;')
    allUsers = crsr.fetchall()

    line = 0
    success = False
    for i in allUsers:
        if i == username:
            success = True
            break
        else:
            continue
    if success == False:
        break #come back to this
    else:
        continue
    crsr.execute('SELECT password FROM accounts;')
    allPass = crsr.fetchall()
    line2 = 0
    success = False
    for i in allPass:
        line2 + 1
        if line2 == line:
            if password == i:
                success = True
                pass
        else: 
            continue
        if success == False:
            break
        else:
            continue

    crsr.execute(f'SELECT role FROM accounts WHERE password={password}')
    role = crsr.fetchall()
    s.send(role.encode())

    clientsockets.add(client_socket)

    
    t = Thread(target=listenforclient, args=(client_socket,))

    t.daemon = True
    t.start()
    

    
    
for cs in clientsockets:
    cs.close()
s.close()
#""")
#print(clientsockets)









