# The user enters a string containing a number (e.g."45", ). Convert it to:
"""
• an integer
• a float
• a string again
Print all three values with their types """


# Take a number as a string from the user
user_input = input("Enter a string number: ")

# Convert the string into an integer
integer_value = int(user_input)

# Convert the string into a float
float_value = float(user_input)

# Keep the value as a string
string_value = str(user_input)

# Print all values with their data types
print("Integer value:", integer_value, "| Type:", type(integer_value))
print("Float value:", float_value, "| Type:", type(float_value))
print("String value:", string_value, "| Type:", type(string_value))

"""Enter a string number: 45
Integer value: 45 | Type: <class 'int'>
Float value: 45.0 | Type: <class 'float'>
String value: 45 | Type: <class 'str'>"""