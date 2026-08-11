#Rhombus Star Pattern in python ?
"""A rhombus is a quadrilateral whose four sides all have the same length. So, In this pattern, numbers of rows and equal number of columns are present. So, User have to enter a single value, that will be determine as a number of rows and columns of the pattern."""

num = int(input("Enter the number:"))

for i in range(0, num):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, num):
        print("*", end="")
    print()

# This code is contributed by Shubhanshu Arya (Prepinsta Placement Cell Student) 