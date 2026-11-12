#. Python File Handling – Write and Read Names

# Step 1: Open the file in write mode
file = open("names.txt", "w")

# Step 2: Enter 5 names from the user
print("Enter 5 names:")

for i in range(5):
    name = input("Enter name: ")
    file.write(name + "\n")

# Step 3: Close the file
file.close()

# Step 4: Open the same file in read mode
file = open("names.txt", "r")

# Step 5: Read and display all names
print("\nNames stored in the file:")

for name in file:
    print(name.strip())

# Step 6: Close the file
file.close()
