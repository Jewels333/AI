import socket

clientsocket = socket.socket()
port = 12345
clientsocket.connect(('127.0.0.1',port))

#recieve connection message from server
recvmsg = clientsocket.recv(1024)
print(recvmsg)

#send user details to server
send_msg = input("Enter your user name(prefix with #):")
clientsocket.send(send_msg)


#receive and send message from/to different user/s

while True:
    recvmsg = clientsocket.recv(1024)
    print(recvmsg)
    sendmsg = input("Send your message in format [@user:message] ")
    if sendmsg == 'exit':
        break;
    else:
        clientsocket.send(send_msg)

clientsocket.close()