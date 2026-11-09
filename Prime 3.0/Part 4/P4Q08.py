# Q8. Player Class Using Class Variables and Instance Variables in Python

class Player:

    # Class variable
    player_count = 0

    def __init__(self, name, level):

        # Instance variables
        self.name = name
        self.level = level

        # Increase player count whenever an object is created
        Player.player_count += 1

    # Display player details
    def display(self):
        print("Player Name:", self.name)
        print("Player Level:", self.level)


# Creating player objects
p1 = Player("Rahul", 5)
p2 = Player("Amit", 10)
p3 = Player("Priya", 15)

# Display player details
print("Player 1:")
p1.display()

print("\nPlayer 2:")
p2.display()

print("\nPlayer 3:")
p3.display()

# Display total number of players
print("\nTotal Players Created:", Player.player_count)


#OUTPUT
"""Player 1:
Player Name: Rahul
Player Level: 5

Player 2:
Player Name: Amit
Player Level: 10

Player 3:
Player Name: Priya
Player Level: 15

Total Players Created: 3
PS D:\Python> """