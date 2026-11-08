# Program: Abstract Class – Employee
# Concept: Abstraction and Abstract Methods


from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass


# Child Class 1: Intern
class Intern(Employee):

    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend


# Child Class 2: FullTimeEmployee
class FullTimeEmployee(Employee):

    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# Child Class 3: ContractEmployee
class ContractEmployee(Employee):

    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Creating objects
intern = Intern("Rahul", 10000)

fulltime = FullTimeEmployee("Amit", 50000)

contract = ContractEmployee("Priya", 500, 80)


# Displaying salaries
print("Employee Salary Details")

print("Intern:", intern.name)
print("Salary:", intern.calculate_salary())

print("\nFull Time Employee:", fulltime.name)
print("Salary:", fulltime.calculate_salary())

print("\nContract Employee:", contract.name)
print("Salary:", contract.calculate_salary())


"""PS D:\Python> & 'C:\Users\jayendra kumar\AppData\Local\Python\pythoncore-3.14-64\python.exe' 'd:/Python/prime3.0/P4Q06.py'
Employee Salary Details
Intern: Rahul
Salary: 10000

Full Time Employee: Amit
Salary: 50000

Contract Employee: Priya
Salary: 40000
PS D:\Python> """