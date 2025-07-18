# Create a program that takes two numbers and an operator (+, -, *, /) and performs the operation
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
op = input("Enter the operator (+, -, *, /): ")

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("INVALID INPUT: Cannot divide by zero.")
else:
    print("INVALID INPUT: Unknown operator.")
