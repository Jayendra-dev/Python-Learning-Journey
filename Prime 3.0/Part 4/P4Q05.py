# Program: Inheritance (Vehicle, Car and Bike)
# Base class
class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Child class Car
class Car(Vehicle):

    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_car(self):
        self.display()
        print("Number of Seats:", self.seats)


# Child class Bike
class Bike(Vehicle):

    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_bike(self):
        self.display()
        print("Engine CC:", self.engine_cc)


# Creating objects
car1 = Car("Toyota", "Fortuner", 7)
bike1 = Bike("Royal Enfield", "Classic 350", 350)

# Displaying details
print("---- Car Details ----")
car1.display_car()

print("\n---- Bike Details ----")
bike1.display_bike()
Program: Inheritance (Vehicle, Car and Bike)


"""---- Car Details ----
Brand: Toyota
Model: Fortuner
Number of Seats: 7

---- Bike Details ----
Brand: Royal Enfield
Model: Classic 350
Engine CC: 350"""