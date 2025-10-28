# Youtube: https://www.youtube.com/watch?si=HNq2HzhlahVirB02&v=Ej_02ICOIgs&feature=youtu.be

# A class is a blueprint for creating objects. It defines what attributes/data/methods/functions that the objects create using this class
class Dog:
    # Methods or Functions defines what actions or behavior the object can perform. 
    def __init__(self, name, breed, owner):
    # Self is a keyword used to access the specific object's attributes or methods inside the class. When we initiate the  
    # dog1 object then control goes to Dog class and since self is there it considers the values we gave to dog1 object as 
    # the current values to this Dog class
        self.dogname = name
        self.breed = breed
        self.owner = owner
    def bark(self):
        print("Whoof Whoof")

class Owner:
    def __init__(self, name, address, number):
        self.ownername = name
        self.address = address
        self.contactnumber = number

# An Object is an instance of an class. owner1 is an object created form the Owner Class with its blueprint using set of data
owner1 = Owner("Varun", "Vizianagaram", "9182575998")
owner2 = Owner("Tej", "Vizianagaram", "9182575668")

dog1 = Dog("Ramu", "Pomerenian", owner1) # passing owner1 object as an parameter to dog1 object
dog1.bark()
print(dog1.owner.ownername) # can access owner object form dog1 object
print(dog1.owner.address)

print(dog1.breed)
print(dog1.dogname)

dog2 = Dog("Rocky", "Husky", owner2)
dog2.bark()