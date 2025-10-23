############################################
### Protected and Private Methods
### 
### 
### 
############################################

class BankAccount:
    MIN_BALANCE = 100  # static attributes
    def __init__(self, owner, balance = 0):
        self.owner = owner   # instance attributes
        self._balance  = balance
    def  deposit(self, amount):
         if self._is_valid_amount(amount): # if true
             self._balance += amount
             self.__log_transaction("deposit", amount)
         else:
             print("Deposit amount must be positive")
    
    def _is_valid_amount(self, amount):   # protected method
        return amount > 0 # returns boolean
    
    def __log_transaction(self, transaction_type, amount):  # private method
        print(f"Logging {transaction_type} of ${amount}. New Balance: $ {self.balance}")


    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5   # interest rate should be between 0 and 5, returns boolean
       

account = BankAccount("Varun", 5000)
account.deposit(200)

account._is_valid_amount(200) # Not suggested to do since it is protected method
# account.__log_transaction("withdraw", 500) # throws error as it is private method and not allowed to access outside the class

print(BankAccount.is_valid_interest_rate(3)) # true
print(BankAccount.is_valid_interest_rate(10)) # false