#Q10.Letʼs create a “ ”. Given a secret number (alreadydecided by you), 
# write a program that asks the user to guess it and prints:

''' if the guess is above the number"Too high"
• if the guess is below"Too low"
• if the guess matches"Correct!"


'''



# Number Guessing Game

# Secret number already decided
secret_number = 25

# Ask the user to guess the number
guess = int(input("Guess the secret number: "))

# Check the guess
if guess > secret_number:
    print("Too high")

elif guess < secret_number:
    print("Too low")

else:
    print("Correct!")
    #output:
#Guess the secret number: 25
#Correct!