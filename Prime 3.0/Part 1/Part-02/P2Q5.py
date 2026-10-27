#5 . Write a function to return the sum  of a number,n .

def sum_digits(n):
    total = 0

    while n > 0:
        digit = n % 10      # Get the last digit
        total += digit      # Add digit to total
        n = n // 10         # Remove the last digit

    return total

n = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(n))

#output:
#Enter a number: 12
#Sum of digits: 3