"""Q8.Write a function is_prime(n), that returns  true if n is a prime number and false
otherwise, using a loop."""

def is_prime(n):

    # Prime numbers are greater than 1
    if n <= 1:
        return False

    # Check divisibility using a loop
    for i in range(2, n):

        if n % i == 0:
            return False

    return True


# Taking input from user
num = int(input("Enter a number: "))

# Function calling
if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
