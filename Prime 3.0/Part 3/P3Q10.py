#  Ask the user for a string and print:
#• All unique characters
#• The count of unique characters


# Ask the user to enter a string
text = input("Enter a string: ")

# Find all unique characters using set()
unique_chars = set(text)

# Print unique characters
print("Unique characters:", unique_chars)

# Count unique characters
print("Count of unique characters:", len(unique_chars))



# output:
# Enter a string: jayendra kuamar iks learnjinf python 
# Unique characters: {'k', ' ', 'n', 'u', 'p', 'l', 'a', 's', 'o', 'j', 'r', 'y', 'i', 'e', 'h', 't', 'd', 'f', 'm'}
# Count of unique characters: 19
