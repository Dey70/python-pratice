print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height > 120:
    print("Yes, you're allowed to ride!")

    age = int(input("What is your age? "))
    if age < 12:
        print("The ride would be $5")
    elif age > 12 and age < 18:
        print("The ride would be $7")
    else:
        print("The ride would be $12")

else:
    print("No! you're not allowed to ride!")
