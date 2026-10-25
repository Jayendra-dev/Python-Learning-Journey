
# Program to swap two numbers entered
#  by the user

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Print original values before swapping
print("Before swapping:", a, b)

# Swap the values using a temporary variable
temp = a
a = b
b = temp

# Print updated values after swapping
print("After swapping:", a, b)


""" output:
Enter first number: 11
Enter second number: 12
Before swapping: 11 12
After swapping: 12 11"""