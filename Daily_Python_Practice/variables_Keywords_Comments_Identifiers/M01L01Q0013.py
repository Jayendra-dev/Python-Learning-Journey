"""3. Shadow Trap – Variable Shadowing in Python
A. What is variable shadowing?
Variable shadowing occurs when a variable declared inside a 
function uses the same name as a variable from an outer scope or a built-in Python name.

Python has a built-in function called max() that returns the largest value from a collection."""
# Corrected code

maximum_value = 100

numbers = [10, 20, 50, 30]

largest_number = max(numbers)

print("Maximum value:", largest_number)
print("Stored value:", maximum_value)

# Maximum value: 50
# Stored value: 100
