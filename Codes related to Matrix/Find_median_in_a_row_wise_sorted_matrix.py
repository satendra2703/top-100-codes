#Find median in a row wise sorted matrix in python ?
"""we will learn how to Find the Median of Row Wise Sorted Matrix in Python.

Example :

Input :   arr  =  [  [ 1, 3, 5 ], [ 2, 6, 9 ], [ 3, 6, 9 ]  ]
Output :   5 """

mat = [[1, 3, 5],
       [2, 6, 9],
       [3, 6, 9]]

arr = []

for i in range(3):
    for j in range(3):
        arr.append(mat[i][j])

arr.sort()

print("Median of the given matrix is :", arr[4])