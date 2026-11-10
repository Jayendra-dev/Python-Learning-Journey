
# Parent Class 1
class Herbivore:
    def __init__(self):
        self.plant_food = "Grass, Fruits and Leaves"

    def eat_plants(self):
        print("Eats:", self.plant_food)


# Parent Class 2
class Carnivore:
    def __init__(self):
        self.meat_food = "Fish and Small Animals"

    def eat_meat(self):
        print("Eats:", self.meat_food)


# Parent Class 3
class Omnivore:
    def __init__(self):
        self.food_type = "Both Plants and Animals"

    def show_diet(self):
        print("Diet Type:", self.food_type)


# Child Class inheriting from all three classes
class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name, age):
        Herbivore.__init__(self)
        Carnivore.__init__(self)
        Omnivore.__init__(self)

        self.name = name
        self.age = age

    def display(self):
        print("Bear Name:", self.name)
        print("Bear Age:", self.age)


# Creating an object of Bear
b1 = Bear("Brown Bear", 5)

# Accessing attributes and methods
b1.display()
b1.eat_plants()
b1.eat_meat()
b1.show_diet()


"""OUTPUT:
Bear Name: Brown Bear
Bear Age: 5
Eats: Grass, Fruits and Leaves
Eats: Fish and Small Animals
Diet Type: Both Plants and Animals"""