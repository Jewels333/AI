
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

if LoginPass == Password: 
    print('Welcome to chat.')
    menu1 = input('J)oin Room\nC)reate Room\n')
    if menu1 == 'J':
        try:
        
            roomsMenu = input('Enter room name:')
            f = open ( 'apps/chat/rooms/' + roomsMenu + '.txt')

        except FileNotFoundError():
            print('Room not found.')

