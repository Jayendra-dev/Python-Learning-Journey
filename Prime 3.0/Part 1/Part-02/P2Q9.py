''' Q9.Letʼs create a Simple calculator that performs arithmetic operations. Create
a function calculator(a,b,operation) that performs addition, subtraction,
multiplication, or division based on  the Operation parameter.
 parameter can have values , , & .operation ‘+’ ‘-’ '*’ ‘/’.
'''

def calculator(a, b, operation):

    if operation == '+':
        return a + b

    elif operation == '-':
        return a - b

    elif operation == '*':
        return a * b

    elif operation == '/':
        if b == 0:
            return "Error: Division by zero is not allowed"
        return a / b

    else:
        return "Invalid operator"


# Taking input from user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Function calling
result = calculator(a, b, operation)

print("Result:", result)
"""OUTPUT:
Enter first number: 50
Enter second number: 25
Enter operation (+, -, *, /): +
Result: 75.0"""