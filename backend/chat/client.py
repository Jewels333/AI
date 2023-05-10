import socket
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back

init()
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]
clientcolor = random.choice(colors)

serverhost = "127.0.0.1"
serverport = 3333
separatortoken = "<SEP>"

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