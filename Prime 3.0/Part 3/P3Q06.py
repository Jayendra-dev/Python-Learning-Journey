"""#. Given a list of words:
words = ["apple", "banana", "kiwi", "cherry", "mango"]
 Create a dictionary that maps each word to its length.
 Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...}"""



words = ["apple", "banana", "kiwi", "cherry", "mango"]

# Create a dictionary using dictionary comprehension
word_length = {word: len(word) for word in words}

# Display the dictionary
print(word_length)

# {'apple': 5, 'banana': 6, 'kiwi': 4, 'cherry': 6, 'mango': 5}

# solution 2
words = ["apple", "banana", "kiwi", "cherry", "mango"]

result = {}

for word in words:
    result[word] = len(word)

print(result)


#{'apple': 5, 'banana': 6, 'kiwi': 4, 'cherry': 6, 'mango': 5}
 