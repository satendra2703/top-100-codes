#Find Second Smallest Element in an Array using pyhton ?
"""we are given with an array elements and we need to print the second smallest among the given elements. If we want to find second smallest element from the array enter by the user so we have to compare one element to other until we get the desired element and print it."""

import math 

arr = [10, 13, 17, 11, 34, 21]
first = math.inf
second = math.inf

for i in range(len(arr)):
    if arr[i] < first :
        first = arr[i]

for i in range(len(arr)):
    if arr[i] != first and arr[i] < second:
        second = arr[i]

print("Second smallest element in the array is:", second)