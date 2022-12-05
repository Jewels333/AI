aiName1 = 'Mark'
aiName2 = 'Patrica'
print('Hello World')
name = input('Whats your name?')
print('Hi', name)
print('What do you need?')
option1 = input('(1) Math (2)Coming soon (3)GUI')
if option1 == '1':
  def add(num1,num2):
    answer = num1 + num2
    return answer


  def subtract(num1,hum2):
    answer = num1 - num2
    return answer
  first = int(input("Enter your first number: "))
  second = int(input("Enter your second number: "))

  print("Choose an option: (1) Add, (2) Subtract, (3) Divide, (4) Multiply")
  choice= int(input())

  if choice == 1:
    answer = add(first,second)

  if choice == 2:
    answer = subtract(first, second)


  print("The answer is",answer)

##TASK 1: Add 2 more functions to the calcluator
 #divide
 #multiply
#Complete the if / elif blocks to finish the program

if option1 == '2':
    f = open("errors/error.txt", "r")
    print(f.read()) 
    f.close()
    print("Dont't choose this next time.")
if option1 == '3':
  from tkinter import *
  from tkinter import ttk