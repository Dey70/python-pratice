#Functions with Output Parameters
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "INVALID"

symbols = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
        print(r"""
     _____________________
    |  _________________  |
    | | Calculator   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """)
        num1 = float(input("Enter the first number: "))
        should_continue = True
        while should_continue:
            for symbol in symbols:
                print(symbol)
            operations_symbols = input("Enter a operator: ")
            num2 = float(input("Enter the second number :"))
            answer = symbols[operations_symbols](num1, num2)
            print(f"{num1} {operations_symbols} {num2} = {answer}")

            choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()

            if choice == "y":
                num1 = answer
            else:
                should_continue = False
                print("\n" * 10)
                calculator()
calculator()