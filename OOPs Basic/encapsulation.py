class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
acc = Account()
acc.deposit(1000)
print(acc.get_balance())  # Output: 1000