#Print elements in sorted order using row-column wise sorted matrix in python ?
"""we will learn how to Print elements in sorted order using row-column wise sorted matrix in Python."""
"""we will discuss the program to Print Elements in Sorted Order using Row-Column wise Sorted Matrix in Python programming language. We are given a matrix in which each row and column are sorted in a non-decreasing manner."""

Matrix = [[1, 20, 43, 14],
          [50, 69, 17, 81],
          [99, 10, 11, 22],
          [13, 54, 95, 16]]

arr = []
x, n, m = 0, 4, 4

for i in range(n):
    for j in range(m):
        arr.append(Matrix[i][j])

size = n*m
arr.sort()

for i in range(size):
    print(arr[i], end=" ")