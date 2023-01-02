print('Welcome to the Scripted terminal.')
AccessInput = input('Enter Access Key:\n')
f = open('terminal/access.key')
AccessKey = f.read()
f.close()
if AccessInput == AccessKey:
    print('Welcome.')
    
    LoginName = input('Enter Username:')
    LoginPass = input('Enter Password:')

    terminalFolder = 'terminal/'
    accountsFolder = 'accounts/'

    f = open(terminalFolder + accountsFolder + LoginName + ".key", "r")
    length1 = 1
    Password = (f.readline())
    PasswordLen = len(Password) - 1
    Password = Password[:PasswordLen]
    f.close()

    if LoginPass == Password: #* Issue resovled

        print('Logged in.')

        menu1 = input('(1) Manage Accounts\n(2) Edit Files\n(3) Developer Chat\n')
        if menu1 == '1':
            
            accountManaged = input('What account to manage?')
            try:
                
                f.open(terminalFolder + accountsFolder + accountManaged + ".key")
                
                # TODO: finish menu
                accountMenu = input('Would you like to:\nR)ead info\nA)dd info')
                
                if accountMenu == 'R':
                    f.read()

                elif accountMenu == 'A':
                    infoAdd = input('What to add?')
                    f.append(infoAdd)

            except:
                print('Account not found.')

        elif menu1 == '2':
            print('Editing Files.')
            fileToEdit = input('Enter file to edit:\n')
            try:
                f = open(fileToEdit)
                editStyle = input('Would you like to:\nA)ppend\nW)rite\nR)ead\n')
               
                if editStyle == 'A':
                    appendValue = input('What to add?')
                    f.append('\n' + appendValue)
                    print('Added.')
                
                elif editStyle == 'W':
                    writeValue = input('What to write?')
                    f.write(writeValue)
                    print('Written.')
                
                elif editStyle == 'R':
                    print(f.read())
                    print('Read.')
            except:
               
                noFileFound = input('No file found. Create? (Y/N)\n')
                
                if noFileFound == 'Y':
                    f = open(fileToEdit + '.txt', "x")
                    print('Created, try again.')

                else:
                    print('Canceled.')
        elif menu1 == '3':
            
           import socket
           import sys
           import time
           socket_server = socket.socket()
           server_host = socket.gethostname()
           ip = socket.gethostbyname(server_host)
           sport = 8080
           print('This is your IP address: ', ip)
           server_host = input('Enter friend\'s IP address:')
           name = input('Enter Friend\'s name: ')
 
           socket_server.connect((server_host, sport))
           socket_server.send(name.encode())
           server_name = socket_server.recv(1024)
           server_name = server_name.decode()
 
           print(server_name,' has joined...')
           while True:
                message = (socket_server.recv(1024)).decode()
                print(server_name, ":", message)
                message = input("Me : ")
                socket_server.send(message.encode())  
    else:
        print('Incorrect.')
        print(Password)
        print(PasswordLen)
        print(LoginPass)
else:
    print('Incorrect.')
