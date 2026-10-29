
# Input numbers continuously until the user enters "Quit"

while True:
    user_input = input("Enter a number or 'Quit' to exit: ")

    if user_input == "Quit":
        print("Program terminated.")
        break

    n = int(user_input)

    if n > 0:
        print(n, "is positive")
    elif n < 0:
        print(n, "is negative")
    else:
        print(n, "is zero")


'''
output:
Enter a number or 'Quit' to exit: 1
1 is positive
Enter a number or 'Quit' to exit: -1
-1 is negative
Enter a number or 'Quit' to exit: 2
2 is positive
Enter a number or 'Quit' to exit: 3
3 is positive
Enter a number or 'Quit' to exit: 4
4 is positive
Enter a number or 'Quit' to exit: 3534
3534 is positive
Enter a number or 'Quit' to exit: Quit
Program terminated.
PS D:\Python> '''