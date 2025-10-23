# Polymorphism - Means having multiple forms

# Polymorphism: Derived form Greek. Poly means Many and Morph means forms
# Real world example: 

class Car:
    def __init__(self, brand, model, year, number_of_doors):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_doors = number_of_doors
    
    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")


class Motorcycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year  = year

    def start_bike(self):
        print("Motorcycle is starting")
    
    def stop_bike(self):
        print("Motorcycle is stopping")

# Car and Motorcycle classes with different methods and attributes

# Create a list of vehicles to inspect
vehicles = [
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2021)
]

# Loop through list of vehicles and inspect  them
for vehicle in vehicles:  #Looping the vehicles list based on Class so that you can use methods of that class individually
    if isinstance(vehicle, Car):  # if the vehicle is of Car then you can call Car related attributes and methods
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
        
    elif isinstance(vehicle, Motorcycle): # if the vehicle is of Motorcycle then you can call Motorcycle related attributes and methods
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    
    else:
        raise Exception("Object is not a valid vehicle")

# output:
# Inspecting Ford Focus (Car)
# Car is starting
# Car is stopping
# Inspecting Honda Scoopy (Motorcycle)
# Motorcycle is starting
# Motorcycle is stopping

# Note: But this is not an effective approach as the vehicle types will increase and so the logic of methods. 
# For loop increases and ifelse condition will also increases.
# Review the next python file for refactored code for the same concept