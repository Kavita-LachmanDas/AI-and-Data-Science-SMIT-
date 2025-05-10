# Create a calculator using conditions,
#  You will take two numbers as input from the user, then ask the user for their choice. 
# Depending on user's choice, you have to perform the operation and print the result.
# comments should be written in the code.





# Assignment Title
print(f"\t \t ****************** CALCULATOR ****************")

# Taking two inputs from the user and converting them to integers
num1 = int(input("enter your number 1 :  "))
num2 = int(input('enter your number 2 :   '))

# Displaying operation choices to the user
print(f"Choice 1. Addition 2. Subtraction 3. Multiplication 4. division 5. Floor Division 6. Exponential")

#Taking user's choice of operation
choice = int(input('enter the number of the operation you want to perform: '))

# Performing operation based on user's choice
if choice == 1:
    add = num1 + num2
    print(add)
elif choice == 2:
    sub = num1 - num2
    print(sub)
elif choice == 3:
    mul = num1 * num2
    print(mul)
elif choice == 4:
    div = num1 / num2
    print(div)
elif choice == 5:
    floorDiv = num1 // num2
    print(floorDiv)
elif choice == 6:
    exponential = num1 ** num2
    print(exponential)        

 # Handling invalid choice input
else:
    print("Invalid operator! Please enter a number between 1 and 6.")