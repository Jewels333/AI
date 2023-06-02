import socket,select
port = 3333
socketlist = []
users = {}
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname) 

serversocket.bind((ip,port))
serversocket.listen(5)
print(ip)
socketlist.append(serversocket)

while True:
    readytoread,readytowrite,inerror = select.select(socketlist,[],[],0)
    for sock in readytoread:
        if sock == serversocket:
            connect, addr = serversocket.accept()
            socketlist.append(connect)
            connect.send(bytes("[+] User is connected from:".encode() + str(addr).encode()))
        else:
            try:
                data = sock.recv(2048)
                if data.startswith("#"):
                    users[data[1:].lower()] = connect
                    print("User " + data[1:] +" added.")
                    connect.send("Your user detail saved as : "+str(data[1:]))
                    role = sock.recv(2048)
                elif data.startswith("[@]"):
                    users[data[1:data.index(':')].lower()].send(data[data.index(':')+1:])
                    
            except Exception as e:
                continue

serversocket.close()

