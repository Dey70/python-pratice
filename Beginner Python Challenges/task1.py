# Ask the user for a number and print whether it’s even or odd.
number = int(input("Enter a number: "))
if number%2 ==0:
    print(f"{number}, it is even.")
else:
    print(f"{number}, it is odd.")