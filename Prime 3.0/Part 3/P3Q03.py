# Q3.input two lists of integers from the user. Merge them into one list and sort the result.
# Eg - ,list1 = [1, 2, 7] list2 = [2, 4, 5]
# result = [1, 2, 3, 54, 5, 7]

# Input first list from the user
list1 = list(map(int, input("Enter elements of first list: ").split()))

# Input second list from the user
list2 = list(map(int, input("Enter elements of second list: ").split()))

# Merge both lists
result = list1 + list2

# Sort the merged list
result.sort()

# Display the final result
print("Merged and sorted list:", result)


"""OUTPUT:
Enter elements of first list: 1 2 3 4 5 
Enter elements of second list: 4
Merged and sorted list: [1, 2, 3, 4, 4, 5]"""