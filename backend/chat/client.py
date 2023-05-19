#flask --app backend/chat/app run --host=0.0.0.0 for local
import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back
import sqlite3
init()
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

serverhost = input('Enter host:')
serverport = int(input('Enter port:'))
separatortoken = "<SEP>"
s = socket.socket()
lines = 0

print(f"[*] Connecting to {serverhost}:{serverport}...")

s.connect((serverhost, serverport))
print("[+] Connected.")
username = input('Enter username: ')
password = input('Enter password: ')
password = str(password.encode())
username = str(username.encode())
s.send(username.encode())
s.send(password.encode())
# gonna remake this soon



def listenformessages():
    while True:
        message = s.recv(1024).decode()
        print(message)
        lines.__add__(1)


t = Thread(target=listenformessages)
t.daemon = True
t.start()

while True:
    tosend = input()
    #shell
    if tosend.startswith('script ') and admin == 1:
        #if tosend starts with 'script' and user is admin:
        if tosend == 'script menu':
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

                    


    if tosend.lower() == 'q':
        break
    #if censored in tosend:
    #    break1
    lines.__add__(1)
    datenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    tosend = f"{clientcolor}[{datenow}] {name}{separatortoken}{tosend}{Fore.RESET}"
    s.send(tosend.encode())
    
s.close()
