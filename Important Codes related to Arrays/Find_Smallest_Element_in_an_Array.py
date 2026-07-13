#Find Smallest Element in an Array in python ?
"""we are given with an array elements and we need to print the smallest among the given elements. If we want to find smallest element from the array enter by the user so we have to compare one element to other until we get the desired element and print it."""

a = [10, 20, 4, 45, 99]
min_element = a[0]

for i in range(len(a)):
    if a[i] < min_element:
        min_element = a[i]

print("Smallest element in the array is:", min_element)