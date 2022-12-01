aiName1 = 'Mark'
aiName2 = 'Patrica'
print('Hello World')
name = input('Whats your name?')
print('Hi', name)
print('What do you need', name )
option1 = input('(1) Math (2)Coming soon (3)GUI')
if option1 == '1':
  #f = open("calculator.py", "r")
  #print(f.read()) 
  #f.close()
  print('e')
if option1 == '2':
    f = open("errors/error.txt", "r")
    print(f.read()) 
    f.close()
    print("Dont't choose this next time.")
if option1 == '3':
  import platform 
  print(platform.uname())
 # import tkinter as tk
  #window = tk.Tk()
# hello_world.py
#!/usr/bin/python

