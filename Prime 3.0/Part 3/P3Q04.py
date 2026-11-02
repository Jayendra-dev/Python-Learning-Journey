#  Q4.Given a tuple of integers, create:
# A tuple of all even numbers
# • A tuple of all odd numbers

# Given tuple of integers
numbers = (10, 15, 20, 25, 30, 35, 40, 45)

# Create empty lists
even = []
odd = []

# Check each number in the tuple
for i in numbers:

    # Check whether number is even
    if i % 2 == 0:
        even.append(i)

    # Otherwise, number is odd
    else:
        odd.append(i)

# Convert lists into tuples
even_tuple = tuple(even)
odd_tuple = tuple(odd)

# Display results
print("Original Tuple:", numbers)
print("Even Numbers Tuple:", even_tuple)
print("Odd Numbers Tuple:", odd_tuple)


"""OUTPUT:
Original Tuple: (10, 15, 20, 25, 30, 35, 40, 45)
Even Numbers Tuple: (10, 20, 30, 40)
Odd Numbers Tuple: (15, 25, 35, 45)"""