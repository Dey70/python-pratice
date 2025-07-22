#Print each number from 1 to 5 using a for loop.
for i in range(1,6):
    print(i)

#Write a for loop that prints each character in the word "python".

for i in "python":
    print(i)

#Print the items in the list
fruits = ["apple", "banana", "cherry"]
for item in fruits:
    print(item)

#Print each fruit with its position (starting from 1), like this:
fruits = ["apple", "banana", "cherry"]
for items in range(len(fruits)):
    print(f"{items + 1}. {fruits[items]}")

#Recreate this output using enumerate():
fruits = ["apple", "banana", "cherry"]
for index, item in enumerate(fruits, start=1):
    print(f"{index}. {item}")

    