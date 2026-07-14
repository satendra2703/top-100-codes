#Python program to Sort first half in ascending order and second half in descending order in an array ?
"""We are given with an array and need to print the array in desired sorting way i.e, first half in increasing order and second half in descending order."""

# Python program to print first half in
# Python program to print first half in
# ascending order and the second half
# in descending order


# function to print half of the array in
# ascending order and the other half in
# descending order

def printOrder(arr, n):
    # Sorting the array
    arr.sort()

    # Printing first half in ascending order
    i = 0
    while i < n // 2:
        print(arr[i], end=" ")
        i += 1

    # Printing second half in descending order
    j = n - 1
    while j >= n // 2:
        print(arr[j], end=" ")
        j -= 1


# Driver code
arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
n = len(arr)

printOrder(arr, n)