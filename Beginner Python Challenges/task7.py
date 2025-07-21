"""Challenge 7 – Count Vowels in a Sentence 🔤
🧠 Problem:
Ask the user to enter a sentence. Then count how many vowels are in it (a, e, i, o, u — both uppercase and lowercase).
"""

sentence = input("Enter a sentence: ").lower()
vowel_count = 0
# Using a loop to count vowels
# Uncomment the following lines to use the loop method
# for char in sentence:
#     if char == "a":
#         vowel_count += 1
#     elif char == "e":
#         vowel_count += 1
#     elif char == "i":
#         vowel_count += 1
#     elif char == "o":
#         vowel_count += 1
#     elif char == "u":
#         vowel_count += 1
# print(f"Number of vowels: {vowel_count}")

# Using a more concise method with a single condition
for char in sentence:
    if char in "aeiou":
        vowel_count += 1
print(f"Number of vowels: {vowel_count}")