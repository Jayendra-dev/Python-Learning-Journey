# Q7. Person Class Using Default Parameters in Python

class Person:

    # Constructor with default parameters
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    # Method to display person details
    def display(self):
        print("Name:", self.name)

        if self.age is not None:
            print("Age:", self.age)

        if self.address is not None:
            print("Address:", self.address)


# Creating objects with different arguments

p1 = Person("Rahul")  
p2 = Person("Amit", 21)
p3 = Person("Priya", 22, "Puducherry")

# Display details
print("Person 1:")
p1.display()

print("\nPerson 2:")
p2.display()

print("\nPerson 3:")
p3.display()


#OUTPUT
"""Person 1:
Name: Rahul

Person 2:
Name: Amit
Age: 21

Person 3:
Name: Priya
Age: 22
Address: Puducherry"""