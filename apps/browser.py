import webbrowser
import google
print('Welcome to the Scripted Browser.')

LoginUser = input('Enter username:')
LoginPass = input('Enter password:')
f = open(terminalFolder + accountsFolder + LoginName + ".key", "r")
length1 = 1
Password = (f.readline())
PasswordLen = len(Password) - 1
Password = Password[:PasswordLen]
f.close()

if LoginPass == Password: #* Issue resovled
   print('Welcome to the browser.')
   search = input('Enter search/url:')
   urlDict =  [".www", ".com", ".gov" ".net" ".me" "."]
   if urlDict in search:
     webbrowser.open(search)
   else:
     print(search(search))

   #webbrowser.open()