# Q4. Write a function to return the count the number of digits in a number,n .

# Function to count the digits in a number
def count_digits(n):
    count = 0

    # Special case: zero has one digit
    if n == 0:
        return 1

    # Handle negative numbers
    n = abs(n)

    # Count digits by removing the last digit
    while n > 0:
        count += 1
        n = n // 10

    return count


# Take input from the user
n = int(input("Enter a number: "))

# Call the function and display the result
print("Number of digits:", count_digits(n))

#output:
#Enter a number: 11
#Number of digits: 2