"""
✅ Challenge 9 – Palindrome Checker 🔍
🧠 Problem:
Ask the user to enter a word or sentence.
Check if it reads the same forward and backward.
"""

word = input("Enter a word: ").lower().replace(" ", "")
reversed_word = word[::-1]
if word == reversed_word:
    print(f"It's a palindrome. The reversed word is {reversed_word}")
else:
    print(f"It' not a palindrome. The reversed word is {reversed_word}")