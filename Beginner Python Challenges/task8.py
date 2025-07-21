""""
✅ Challenge 8 – Sum of Digits in a Number 🔢
🧠 Problem:
Ask the user to enter a number (like 547).
Then calculate the sum of its digits (5 + 4 + 7 = 16).


"""

number = input("Enter a number: ")
total_count = 0
for num in number:
    total_count += int(num)
print(f"Sum of the digits : {total_count}")