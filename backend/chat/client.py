import socket

clientsocket = socket.socket()
port = 3333
hostip = input('Enter host:')
clientsocket.connect((hostip,port))

#recieve connection message from server
recvmsg = clientsocket.recv(1024)
print(recvmsg)

#send user details to server
sendmsg = bytes(input("Enter your user name:".encode())) 
clientsocket.send(sendmsg)


#receive and send message from/to different user/s

while True:
    recvmsg = clientsocket.recv(1024)
    print(recvmsg)
    sendmsg = input()
    if sendmsg == 'exit':
        break
    else:
        clientsocket.send(send_msg)

clientsocket.close()