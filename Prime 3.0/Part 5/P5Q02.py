# File Handling – Append and Read Log File
# Step 1: Open the file in append mode
file = open("log.txt", "a")

# Step 2: Add a new log entry
log = input("Enter log entry: ")
file.write(log + "\n")

# Step 3: Close the file
file.close()

# Step 4: Open the file in read mode
file = open("log.txt", "r")

# Step 5: Display all log entries
print("\nAll Log Entries:")

for line in file:
    print(line.strip())

# Step 6: Close the file
file.close()



#OUTPUT:

#Enter log entry: I am learning Python



#All Log Entries:
#program run successfullyprogram run successfullym yname is Jayendra kumar
#I am learning Python
 