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

    f = open( terminalFolder + accountsFolder + LoginName + ".key")

    Password = f.readline() #* It has the correct info, not matching correctly
    if Password == LoginPass: #! 
        print('logged in')
    else:
        print('Incorrect')
        print(Password)
        print(LoginPass)
else:
    print('Incorrect.')
