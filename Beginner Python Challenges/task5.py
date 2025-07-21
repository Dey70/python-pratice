"""
🔁 Challenge 5: Reverse a String
🧠 Problem:
Ask the user to input a string and print it in reverse.
"""

#Slicing
word = input("Enter a word: ")
reverse_word = word[::-1]
print("Reversed word : ", reverse_word)

#Loops
word = input("Enter a word: ")
reversed_word = ""
for letter in word:
    reversed_word = letter + reversed_word
print("Reversed word: ",reversed_word)