# Program: Student Class Using Getters, Setters and Validation

class Student:

    # Constructor
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # Setter method for name
    def set_name(self, name):
        if name.strip() != "":
            self._name = name
        else:
            print("Error: Name cannot be empty!")

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for roll number
    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Error: Roll number must be between 1 and 100!")

    # Getter method for roll number
    def get_roll_no(self):
        return self._roll_no

    # Setter method for marks
    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Error: Marks cannot be negative!")

    # Getter method for marks
    def get_marks(self):
        return self._marks

    # Display student details
    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.get_name())
        print("Roll Number:", self.get_roll_no())
        print("Marks:", self.get_marks())


# Creating Student object
s1 = Student("Jayendra", 25, 85)

# Display details
s1.display()

# Updating values using setter methods
s1.set_name("Rahul")
s1.set_roll_no(50)
s1.set_marks(90)

# Display updated details
print("\nAfter Updating:")
s1.display()


"""output:

--- Student Details ---
Name: Jayendra
Roll Number: 25
Marks: 85

After Updating:

--- Student Details ---
Name: Rahul
Roll Number: 50
Marks: 90
PS D:\Python> """