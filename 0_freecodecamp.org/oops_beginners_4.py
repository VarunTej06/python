############################################
### Protected Parameters, Make data Private
### and use properties
############################################

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    @property # decorator
    def email(self):   # create a property for the protected variable so that protected variable can be accessed outside the class like getter
        print("Email Accessed")
        return self._email
    @email.setter           # setter method
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
    
user1 = User("varun", "varun@gmail.com", "Varun@123" )
user1.email = "sai@outlook.com"
print(user1.email) # accessing the email property not the protected "_email" 
# output: Email accessed /n varun@gmail.com 

# Note:
# 1. No need to use getters and setters if you are using properties
# 2. With only @properties you cannot assign value to email from outside the class like line no
# 3. You need to have a setter for email then only it will work

# output: Once @email.setter is added
# Email Accessed /n sai@outlook.com