############################################
### Static Attributes
### A static attribute (sometimes called as class attribute) is an attribute
### that belongs to the class itself, not to any specific instance of the class.
############################################

class User:
    user_count = 0  # static attributes
    def __init__(self, username, email):
        self.username = username   # instance attributes
        self.email  = email
        User.user_count += 1
    def  display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user1 = User("varun", "varun@gmail.com")
user2 = User("sai", "tej@gmail.com")
print(User.user_count) # output: 2 everytime we initiate an object init method updates the user_count static variable
# above line you are accessing it directly form class

# now lets access it form user instances we created
print(user1.user_count) # output: 2
print(user2.user_count) # output: 2