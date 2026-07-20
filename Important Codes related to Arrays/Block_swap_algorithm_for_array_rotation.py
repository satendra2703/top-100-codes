#Block swap algorithm for array rotation in python ?
"""It is one of the most efficient algorithms used for array rotation. Now, let’s discuss about block swap algorithm and a program to rotate an array using the same algorithm."""

def swap(arr, fi, si, d):
    for i in range(d):
        arr[fi + i], arr[si + i] = arr[si + i], arr[fi + i]


def leftRotateRec(arr, i, d, n):
    # Base cases
    if d == 0 or d == n:
        return

    # If both blocks are of same size
    if n - d == d:
        swap(arr, i, n - d + i, d)
        return

    # If A is shorter
    if d < n - d:
        swap(arr, i, n - d + i, d)
        leftRotateRec(arr, i, d, n - d)

    # If B is shorter
    else:
        swap(arr, i, d + i, n - d)
        leftRotateRec(arr, n - d + i, 2 * d - n, d)


def leftRotate(arr, d):
    n = len(arr)
    leftRotateRec(arr, 0, d, n)


# Driver Code
arr = [10, 20, 30, 40, 50, 60, 70]

d = 2
leftRotate(arr, d)

print("Array after left rotation:")
print(*arr)