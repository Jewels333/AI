import socket

clientsocket = socket.socket()
port = 3333
hostip = input('Enter host:')
clientsocket.connect((hostip,port))
role = 'admin'
#recieve connection message from server
recvmsg = clientsocket.recv(1024)
print(recvmsg)

#send user details to server
sendmsg = bytes(input("Enter your user name:").encode()) 
name = sendmsg
newUser = bytes(str('[#] ').encode())
clientsocket.send( newUser + sendmsg)



#receive and send message from/to different user/s

#formats
def format(role, msg):
    if role == 'user':
        return f'[@] {name}: {msg}'

while True:
    recvmsg = clientsocket.recv(1024)
    print(recvmsg)
    sendmsg = bytes(str(role).encode())
    clientsocket.send(sendmsg)
    sendmsg = bytes(input().encode())
    if sendmsg == 'script exit':
        break
    else:
        clientsocket.send(bytes(format('user', sendmsg).encode()))


clientsocket.close()