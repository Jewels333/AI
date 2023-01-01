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
        print('logged in')
        
    else:
        print('Incorrect.')
        print(Password)
        print(PasswordLen)
        print(LoginPass)
else:
    print('Incorrect.')
