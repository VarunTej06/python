############################################
### Protected Parameters, Make data Private
### and use getters and setters
############################################

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def say_hi_to_user(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username} its {self.username}"
            )

user1 = User("varun", "varun@gmail.com", "Varun@123" )
user2 = User("sai", "sai@gmail.com", "sai@123" )
# User1 wants to say Hi to user2

user1.say_hi_to_user(user2) # Output: Sending message to sai: Hi sai its varun (this is varun here because we are calling this method from user1 object)

# you can modify values 
print(user1.email) # output: varun@gmail.com
user1.email = "dan" # not a correct syntax for email
print(user1.email) # output: dan

# So, lets make this attribute protected. Once protected it will be accessible only insde the class. but python allows outside the class as well (bug)
# just add _ before the attribute inside the class then it becomes protected attribute


# Example for Protected:

class Customer:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email # Add underscore
        self.password = password

    def clean_email(self):
        return self._email.lower().strip()
    
customer1 = Customer("varuntej", " Vartj12@gmail.com ", "1234")
print(customer1._email) # Not supposed to do. python expects the developers will not do this. Consenting Adults philosophy followed by python for this.
print(customer1.clean_email()) # output: vartj12@gmail.com

# You can add double underscore in lines 37, 41, 44. So that the variable now becomes Private and cant be accessed outside the class
# Line 44 will not work then.

# Can access the Protected variables using getter and setters outside the class
# Explaination for that with different example

from datetime import datetime

class Client:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password
    
    def get_email(self): # add get to the variable _email
        print(f"Email accessed at {datetime.now()}")
        return self._email
    def set_email(self, new_email): # add set to the variable name
        if "@" in new_email:  #validation to set an email
            self._email = new_email


client1 = Client("Teja", "tej@gmail.com", "456")
print(client1.get_email()) # output: Email accessed at 2025-10-21 02:21:02.295897 /n tej@gmail.com

client1._email = "1234455" # Updating outside the class is Possible but not supposed to do since it is protected variable
# If you want to modify it form outside the class, add setter as well to the variable and then 
client1.set_email("varuntej1045@gamil.com")
print(client1.get_email()) # output: Email accessed at 2025-10-21 02:21:02.296055 /n varuntej1045@gmail.com

client1.set_email("vargamil.com") # will not assign value due to validation
print(client1.get_email()) # output: Email accessed at 2025-10-21 02:21:02.296055 /n varuntej1045@gmail.com
