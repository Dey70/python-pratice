# Ask the user to enter three numbers, then print out which one is the largest.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

num_list = [num1, num2, num3]
highest_number = max(num_list)

print(f"The highest number is: {highest_number}")

# Alternatively, using if-else statements
if num1 >= num2 and num1 >= num3:
    highest = num1
elif num2 >= num1 and num2 >= num3:
    highest = num2
else:
    highest = num3

print(f"The highest number is: {highest}")