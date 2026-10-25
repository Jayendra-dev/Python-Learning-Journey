''' Q1. Write a program that takes as input. Using conditional statements,
calculate the based on these rules:
 If salary < 30,000 → 5%
• If salary is 30,000 – 70,000 → 15%
• If salary > 70,000 → 25% '''

# Take salary as input from the user
salary = float(input("Enter your salary: ₹"))

# Calculate tax rate based on salary
if salary < 30000:
    tax_rate = 5
elif salary <= 70000:
    tax_rate = 15
else:
    tax_rate = 25

# Calculate tax amount
tax = salary * tax_rate / 100

# Display the results
print("Salary: ₹", salary)
print("Tax Rate:", tax_rate, "%")
print("Tax Amount: ₹", tax)


'''Enter your salary: ₹1000000
Salary: ₹ 1000000.0
Tax Rate: 25 %
Tax Amount: ₹ 250000.0'''
