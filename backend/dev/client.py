class tool:
    def encode(str, type):
        
        charList = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                    '1','2','3','4','5','6','7','8','9','0',
                    '`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[','{',']','}','|',';',':','"',"'",'<','>',',','.','?','/'}
        if type == 'USC-1': #User Standard Code 1
            strLen = len(str)
            
        if type == 'ASC-2': #Admin Standard Code 2
            strLen = len(str)
            encoded = ''
            for element in str:
               with charList as letters:
                charListIndex = letters.find(element) 
                char = charListIndex
                
               encoded = element, end=' '

                
    def decode(str, type):
        pass
print('Welcome to the Developer Portal.')
input = input('Enter your access key:')
f = open('apps/dev/terminal/access.key')
key = f.readline()
if input == key:
    user == input('Enter username:')
    verificate  == input('Enter verification key:')
    userVKey = ''
    if verificate == userVKey:
        with user as user:
            print('Welcome {name}.')
            menu = input('')
    #skipped 


