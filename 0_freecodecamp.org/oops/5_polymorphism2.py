class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def start(self):
        print("Vehicle is Starting")
    def stop(self):
        print("Vehicle is Stoping")

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year) # usig super we are passing the values to super class init method
        self.number_of_doors = number_of_doors
    
    # You can use same method as Vehicle class to override the logic of it form Car class itself
    def start(self):
        print("Car is starting")  

    def stop(self):
        print("Car is stopping")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def start(self):
        print("Motorcycle is starting")
    
    def stop(self):
        print("Motorcycle is stopping")

vehicles = [  # all the vehicle types are treated as vehicle irrespective of vehicle type
    Car("Ford", "Focus", 2008, 5),
    Motorcycle("Honda", "Scoopy", 2021)
]

# vehicles: list[Vehicle] = [
#     Car("Ford", "Focus", 2008, 5),
#     Motorcycle("Honda", "Scoopy", 2021)
# ]

for vehicle in vehicles:
    if isinstance(vehicle, Vehicle):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception("Object is not a valid vehicle")

# Simple alternative for loop for the above loop - output will be same for Output 1 and output 2
# update the vehicle declaration as well to the alternative if you want to use this below for loop
# for vehicle in vehicles:
#     print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
#     vehicle.start()
#     vehicle.stop()

# Output 1:
# output if both start and stop methods in Car and Motorcycle class are commented:
# Inspecting Ford Focus (Car)
# Vehicle is Starting
# Vehicle is Stoping
# Inspecting Honda Scoopy (Motorcycle)
# Vehicle is Starting
# Vehicle is Stoping

# Output 2:
# If both are uncommmented in both classes
# Inspecting Ford Focus (Car)
# Car is starting
# Car is stopping
# Inspecting Honda Scoopy (Motorcycle)
# Motorcycle is starting
# Motorcycle is stopping


# You can add another class called Plane that inherits vehicle class and add one more value into vehicle list variable
# Other than that no need to change anything
# you will get the output of the functions form vehicle or plane class