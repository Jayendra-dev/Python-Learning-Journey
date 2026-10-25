#  Q2.Write a function that takes two integers a and b and prints all even
# numbers between them (inclusive).



# Function to print even numbers between a and b
def print_even(a, b):
    for num in range(a, b + 1):
        if num % 2 == 0:
            print(num, end=" ")

# Take input from the user
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Call the function
print_even(a, b)
