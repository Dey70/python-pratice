"""
✅ Challenge 10 – Multiplication Table Generator 🧮
🧠 Problem:
Ask the user for a number.
Print its multiplication table from 1 to 10.
"""


number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} =", i* number)