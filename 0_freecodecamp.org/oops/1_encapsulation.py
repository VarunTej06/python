# Encapsulation

# Encapsulation: It involves Bundling the data/attributes/methods that operates on data into a single unit called a class. 
# Encapsulation helps in hiding the implementation details of the class by only exposing the necessary functionalities to the outside world.
# Real world example: ATM Machine

class BankAccount:
    def __init__(self):
        self._balance = 0.0  # Protecting balance variable for encapsulation

    @property
    def balance(self):     # getter property decorator
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount


# Without knowing internal implementation details we can use the methods/functions of the class like below

account = BankAccount()
print(account.balance)     # accessing the balance property function. Not direct _balance protected variable
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)

# output: 
# 0.0
# 1.99
# 0.99

# Without setter for the property you can not assign the value directly from outside the class
