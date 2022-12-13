aiName1 = 'Mark'
aiName2 = 'Patrica'
print('Hello')
name = input('Whats your name?')
print('Hi', name)
print('What do you need?')
option1 = input('(1) Math (2) Account(3) GUI')
if option1 == '1':
  def add(num1,num2):
    answer = num1 + num2
    return answer


  def subtract(num1,num2):
    answer = num1 - num2
    return answer


  def multiply(num1,num2):
    answer = num1 * num2
    return answer


  def divide(num1,num2):
    answer = num1 / num2
    return answer

  first = int(input("Enter your first number: "))
  second = int(input("Enter your second number: "))

  print("Choose an option: (1) Add, (2) Subtract, (3) Divide, (4) Multiply")
  choice= int(input())

  if choice == 1:
    answer = add(first,second)

  elif choice == 2:
    answer = subtract(first, second)

  elif choice == 3:
    answer = divide(first, second)
  elif choice == 4:
    answer = multiply(first, second)
  print("The answer is",answer)

##TASK 1: Add 2 more functions to the calcluator
 #divide
 #multiply
#Complete the if / elif blocks to finish the program

if option1 == '2':
  option2 = input(' (1) New User (2) Login')
  if option2 == '1':
    userName = input('Enter username:')
    passWord = input('Enter password:')
    folderAccounts = 'accounts/'
    f = open(folderAccounts + userName + ".txt", "x")
    f = open(folderAccounts + userName + ".txt", "w")
    
    f.write(passWord)
    
  if option2 == '2':
    loginUser = input('Enter Username:')
    folderAccounts = 'accounts/'
    
    loginPass = input('Enter Password:')
    
    f = open(folderAccounts + loginUser + ".txt", "r")
    fullstring = f.readline()
    substring = loginPass
    account = folderAccounts + loginUser + '.txt'

    if substring in fullstring:
      print("Logged in.")
      #start new
      
      option3 = input('(1) Check Accounts')
      if option3 == '1':
        checkedUser = input('What account do you want to check?')
        f = open(folderAccounts + checkedUser + ".txt", "r")
        print(f.read())
        print('1: password 2: type of account 3: ID')

        
    else:
      print("Incorrect Password")
    #if loginPass == '':
      #print('login successful')
    #else:
      #print('Login unsuccessful')
   

    