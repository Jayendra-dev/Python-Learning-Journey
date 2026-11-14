# Q5. Program: Exception Handling (File Not Found)

try:
    # Try to open the file in read mode
    file = open("data.txt", "r")

    # Read and display file contents
    content = file.read()
    print(content)

    # Close the file
    file.close()

except FileNotFoundError:
    # Handle the exception if file does not exist
    print("File not found!")
#output:
# pyhthon
# java