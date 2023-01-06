
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
    