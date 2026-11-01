# Q2.Given a list of integers compute the average of all numbers in the list.
# Given list of integers
n = [10, 20, 30, 40, 50]

# Initialize sum
total = 0

# Calculate sum of all numbers
for i in n:
    total += i

# Calculate average
avg = total / len(n)

# Print results
print("Sum =", total)
print("Average =", avg)

