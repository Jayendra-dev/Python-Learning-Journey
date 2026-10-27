'''Write a function that prints the digits of a number, n
 For eg: n=312, there are 3 digits in it 3, 1 and 2 & we need to print them.
 HINT:- The right most digit of a number N is N%10.
 And to remove the right most digit from a number, we can do N = N / 10.]'''



# Function to print the digits of a number

def print_digits(n):
    if n == 0:
        print(0)
        return

    while n > 0:
        digit = n % 10       # Get the rightmost digit
        print(digit)         # Print the digit
        n = n // 10          # Remove the rightmost digit

# Take input from the user
n = int(input("Enter a number: "))

# Call the function
print_digits(n)
