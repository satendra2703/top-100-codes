#Find the Smallest and largest element in an array in python ?
"""we are given with an array elements and we need to print the smallest and largest among the given elements. If we want to find smallest and largest element from the array enter by the user so we have to compare one element to other until we get the desired element and print it."""

arr = [10, 20, 4, 45, 99]
mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
    if arr[i] < mini:
        mini = arr[i]

    if arr[i] > maxi:
        maxi = arr[i]

print("Smallest element in the array is:", mini)
print("Largest element in the array is:", maxi)