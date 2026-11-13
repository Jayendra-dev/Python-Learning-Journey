#Python Program: Filter Numbers Greater Than 15 Using List Comprehension
# Step 1: Create a list of numbers
numbers = [5, 10, 15, 20, 25]

# Step 2: Use list comprehension to filter numbers greater than 15
new_list = [num for num in numbers if num > 15]

# Step 3: Print the new list
print("Numbers greater than 15:", new_list)


#output:Numbers greater than 15: [20, 25]