aiName1 = 'Mark'
aiName2 = 'Patrica'
print('Hello World')
name = input('Whats your name?')
print('Hi', name)
print('What do you need', name )
option1 = input('(1) Math (2)Coming soon')
if option1 == '1':
  f = open("calculator.py", "r")
  print(f.read()) 
  f.close()
if option1 == '2':
    f = open("errors/error.txt", "r")
    print(f.read()) 
    f.close()