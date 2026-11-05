#  Print All Duplicate Elements in a List
# Create a list
my_list = [1, 2, 3, 4, 2, 5, 3, 6, 1]

# Create an empty set to store duplicate elements
duplicates = set()

# Create an empty set to track visited elements
seen = set()

# Check each element
for i in my_list:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

# Print duplicate elements
print("Duplicate elements:", duplicates)

# Duplicate elements: {1, 2, 3}