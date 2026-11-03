# Q5. Student Marks Management System Using Dictionary in Python
'''Write a menu-based Python program to perform different operations on a dictionary 
where student names are keys and marks are integer values.'''




# Student Marks Management System

students = {}

while True:
    print("\n===== STUDENT MARKS MANAGEMENT =====")
    print("A. Add a Student")
    print("B. Update Marks")
    print("C. Search for a Student")
    print("D. Display All Students and Marks")
    print("E. Exit")

    choice = input("Enter your choice (A/B/C/D/E): ").upper()

    # A. Add a student
    if choice == 'A':
        name = input("Enter student name: ")

        if name in students:
            print("Student already exists!")
        else:
            marks = int(input("Enter marks: "))
            students[name] = marks
            print("Student added successfully!")

    # B. Update marks
    elif choice == 'B':
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter updated marks: "))
            students[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    # C. Search for a student
    elif choice == 'C':
        name = input("Enter student name: ")

        if name in students:
            print("Student Name:", name)
            print("Student Marks:", students[name])
        else:
            print("Student not found!")

    # D. Display all students
    elif choice == 'D':
        if students:
            print("\nStudent Name\tMarks")
            print("-------------------------")

            for name, marks in students.items():
                print(name, "\t\t", marks)
        else:
            print("No student records available!")

    # E. Exit
    elif choice == 'E':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")







"""
output:
===== STUDENT MARKS MANAGEMENT =====
A. Add a Student
B. Update Marks
C. Search for a Student
D. Display All Students and Marks
E. Exit
Enter your choice (A/B/C/D/E): a
Enter student name: Jayendra Kumar
Enter marks: 98
Student added successfully!

===== STUDENT MARKS MANAGEMENT =====
A. Add a Student
B. Update Marks
C. Search for a Student
D. Display All Students and Marks
E. Exit
Enter your choice (A/B/C/D/E): b
Enter student name: Jayendra Kumar
Enter updated marks: 100
Marks updated successfully!

===== STUDENT MARKS MANAGEMENT =====
A. Add a Student
B. Update Marks
C. Search for a Student
D. Display All Students and Marks
E. Exit
Enter your choice (A/B/C/D/E): c
Enter student name: Jayendra Kumar
Student Name: Jayendra Kumar
Student Marks: 100

===== STUDENT MARKS MANAGEMENT =====
A. Add a Student
B. Update Marks
C. Search for a Student
D. Display All Students and Marks
E. Exit
Enter your choice (A/B/C/D/E): d

Student Name    Marks
-------------------------
Jayendra Kumar           100

===== STUDENT MARKS MANAGEMENT =====
A. Add a Student
B. Update Marks
C. Search for a Student
D. Display All Students and Marks
E. Exit
Enter your choice (A/B/C/D/E): e
Exiting the program...
PS D:\Python> """