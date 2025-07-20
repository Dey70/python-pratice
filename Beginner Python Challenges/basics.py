#Loops
even = []
for number in range(1,11):
    if number %2 == 0:
        even.append(number)
print(even)

#Functions
def greet(name):
    print(f"Hello {name}!")
greet("Rajdeep")

#If/Else + Logical Operators
num = int(input("Enter a number :"))
if num > 0:
    if num%2 == 0:
        print(f"{num}, it's  a positive even")
    else:
        print(f"{num}, it's positive odd")
else:
    print("Negative")

#Lists
nums = [2, 4, 6, 8, 10]
nums.append(12)
nums.pop(2)
print(nums)
length = len(nums)
print(length)

#Dictionaries
student = {"name": "Raj", "marks": 90}
student["marks"] = 95
student["grade"] = "A"
print(student.items())