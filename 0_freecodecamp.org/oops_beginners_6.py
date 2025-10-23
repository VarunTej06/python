############################################
### Static Methods
### A static method is an method
### that belongs to the class itself, not to any specific instance of the class.
### to define a static method, we use the '@staticmethod' decorator
############################################

class BankAccount:
    MIN_BALANCE = 100  # static attributes
    def __init__(self, owner, balance = 0):
        self.owner = owner   # instance attributes
        self._balance  = balance
    def  deposit(self, amount):
         if amount > 0:
             self._balance += amount
             print(f"{self.owner}'s new balance is: ${self._balance}")
         else:
             print("Reposit amount must be positive")
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5   # interest rate should be between 0 and 5, returns boolean
       

account = BankAccount("Varun", 5000)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3)) # true
print(BankAccount.is_valid_interest_rate(10)) # false