# Program: Function Overriding Using Inheritance

# Parent class
class Shape:

    def area(self):
        print("Area calculation depends on the shape.")


# Child class 1
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    # Overriding area() method
    def area(self):
        return 3.14 * self.radius * self.radius


# Child class 2
class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Overriding area() method
    def area(self):
        return self.length * self.breadth


# Child class 3
class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    # Overriding area() method
    def area(self):
        return 0.5 * self.base * self.height


# Creating objects
c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

# Calling overridden methods
print("Area of Circle:", c.area())
print("Area of Rectangle:", r.area())
print("Area of Triangle:", t.area())




'''
output:
Area of Circle: 78.5
Area of Rectangle: 50
Area of Triangle: 24.0
PS D:\Python> '''