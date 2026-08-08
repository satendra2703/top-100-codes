#Find a specific pair in matrix in python ?
"""we will discuss the program to Find a Specific Pair in Matrix in Python Programming language. Given an n x n matrix mat[n][n] of integers, find the maximum value of mat(c, d) – mat(a, b) overall choices of indexes such that both c > a and d > b."""

N = 5


def findMaxValue(mat):
    maxValue = 0

    for a in range(N - 1):
        for b in range(N - 1):
            for d in range(a + 1, N):
                for e in range(b + 1, N):
                    if maxValue < (mat[d][e] - mat[a][b]):
                        maxValue = mat[d][e] - mat[a][b]
    return maxValue


matrix = [[ 1,  2, -1, -4, -20],
          [-8, -3,  4,  2,   1],
          [ 3,  8,  6,  1,   3],
          [-4, -1,  1,  7,  -6],
          [ 0, -4, 10, -5,   1]]

print("Maximum Value is", findMaxValue(matrix))