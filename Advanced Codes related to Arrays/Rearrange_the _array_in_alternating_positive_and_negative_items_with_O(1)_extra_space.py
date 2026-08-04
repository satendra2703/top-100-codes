#Rearrange the array in alternating positive and negative items with O(1) extra space in python ?
"""In O(n) time complexity.

Example:

Input :  [ 7, 5, -2, 1, -3 ]
Output :  [ -2, 5, -3, 1, 7 ]"""

def rearrange(arr):
    p = 0
    b = 0
    for i in range(len(arr)):
        if b == 1:
            b -= 1
        elif arr[i] < 0:
            arr[i], arr[p] = arr[p], arr[i]
            if p > i:
                b += 1
            p += 2
    return arr


array = [2, 3, -4, -1, 6, -9]
print("After Rearranging :", rearrange(array))