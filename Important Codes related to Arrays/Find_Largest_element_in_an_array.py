#Find Largest element in an array using Python ?
"""we are given with an array elements and we need to print the largest among the given elements. We discuss different methods to find the largest element using python programing language."""

a = [10, 20, 4, 45, 99]
max_element = a[0]
for i in range(len(a)):
    if a[i] > max_element:
        max_element = a[i]

print("Largest element in the array is:", max_element) 