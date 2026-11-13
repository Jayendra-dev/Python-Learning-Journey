# Q4. Python Program: Store and Update City Population Using JSON
import json

# Step 1: Create a dictionary of three cities and their populations
cities = {
    "Delhi": 32000000,
    "Mumbai": 21000000,
    "Chennai": 12000000
}

# Step 2: Save dictionary into cities.json file
with open("cities.json", "w") as file:
    json.dump(cities, file, indent=4)

print("City data saved successfully!")

# Step 3: Load JSON data from the file
with open("cities.json", "r") as file:
    data = json.load(file)

# Step 4: Print each city and its population
print("\nCity Population Details:")

for city, population in data.items():
    print(city, ":", population)

# Step 5: Ask the user for a new city and its population
new_city = input("\nEnter a new city name: ")
new_population = int(input("Enter its population: "))

# Step 6: Update the dictionary
data[new_city] = new_population

# Step 7: Save updated data back into JSON file
with open("cities.json", "w") as file:
    json.dump(data, file, indent=4)

print("\nNew city added successfully!")

# Step 8: Display updated dictionary
print("\nUpdated City Population Details:")

for city, population in data.items():
    print(city, ":", population)


"""City data saved successfully!

City Population Details:
Delhi : 32000000
Mumbai : 21000000
Chennai : 12000000

Enter a new city name: Lakhimpur
Enter its population: 100000

New city added successfully!

Updated City Population Details:
Delhi : 32000000
Mumbai : 21000000
Chennai : 12000000
Lakhimpur : 100000
"""