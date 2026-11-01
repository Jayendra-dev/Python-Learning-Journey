'''Q1.Ask the user for a string and check whether it is a palindrome or not.
A is a string which is same when we read it forward & backward. Eg -
“madam”, “racecar” etc.
palindrome
[ - A palindrome string is equal to the reversed version of the string. We can
use a loop to reverse the string manually.'''


# Ask the user to enter a string
string = input("Enter a string: ")

# Reverse the string using slicing
reverse = string[::-1]

# Check whether original and reversed strings are equal
if string == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")

    # OUTPUT:
    #Enter a string: MADAM   
    #Palindrome
