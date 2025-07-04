print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
cheese = input("Do you want extra cheese? Y or N: ").upper()
bill = 0

if size == 'S':
    print("That would be $15!")
    bill = 15
    if pepperoni == 'Y':
        print("That would cost you extra $2!")
        bill += 2
    if cheese == 'Y':
        print("That would cost you extra $1!")
        bill += 1
    

    print(f"The final bill is {bill}")
    print("THANK YOU!")

elif size == 'M':
    print("That would be $20!")
    bill = 20
    if pepperoni == 'Y':
        print("That would cost you extra $3!")
        bill += 3
    if cheese == 'Y':
        print("That would cost you extra $1!")
        bill += 1


    print(f"The final bill is {bill}")
    print("THANK YOU!")

elif size == 'L':
    print("That would be $25!")
    bill = 25
    if pepperoni == 'Y':
        print("That would cost you extra $3!")
        bill += 3
    if cheese == 'Y':
        print("That would cost you extra $1!")
        bill += 1
    

    print(f"The final bill is {bill}")
    print("THANK YOU!")

else:
    print("INVALID!")