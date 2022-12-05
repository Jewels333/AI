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

##TASK 3: Add 3 more functions to the calcluator:
 #subtract
 #divide
 #multiply
#Complete the if / elif blocks to finish the program
