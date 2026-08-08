#Rotate matrix by 90 degrees in python ?
"""we will discuss the program to rotate a matrix by 90o in Java Programming Language. We are given a row-wise sorted matrix of size r*c, we need to the rotate a matrix by 90o in clockwise direction."""

def reverseRows(mat):
    n = len(mat)

    for i in range(len(mat)):
        for j in range(n // 2):
            temp = mat[i][j]
            mat[i][j] = mat[i][n - j - 1]
            mat[i][n - j - 1] = temp


def transpose(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr[0])):
            temp = arr[j][i]
            arr[j][i] = arr[i][j]
            arr[i][j] = temp


def printMatrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()


def rotate90(arr):
    transpose(arr)
    reverseRows(arr)


# Driver Code
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotate90(arr)
printMatrix(arr)