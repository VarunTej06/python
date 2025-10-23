# Inheritance

# Inheritance: It involves creating new classes (subclasses or derived classes) based on eisting classes (superclasses or base classes)
# Real world example: A  car is a vehicle and a bike is also a vehicle

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.year = year
        self.model = model
    
    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("vehicle is stopping")

class Car(Vehicle): # the Car class should inherit the parameters and methods from Vehicle class
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year) # To call the init method of Vehicle Class, use super function. Passing values to super class init method
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

car = Car("Ford", "Focus", 2008, 5, 4)
bike = Bike("Honda", "CBZ", 2018, 2)
print(car.__dict__) # Its a dictonary used for objects. We can see all the values of object in dictionary format
print(bike.__dict__)
car.start() # we can call methods of Vehicle class from car object because of Inheritance
bike.stop()

# output:
# {'brand': 'Ford', 'year': 2008, 'model': 'Focus', 'number_of_doors': 5, 'number_of_wheels': 4}
# {'brand': 'Honda', 'year': 2018, 'model': 'CBZ', 'number_of_wheels': 2}
# Vehicle is starting
# vehicle is stopping