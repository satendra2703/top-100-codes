#Merge 2 sorted arrays without using extra space in python ?
"""In this article we will see a python program to Merge 2 sorted arrays. We will given two array namely array1 and array2 of length n1 and n2. Without using any extra list or set or container, we need to merge both the array in such a way that after sorting no element is more then once in the list. And the initial n1 elements of this array after merging is required to be stored in array1 and rest in array2."""

# Merge 2 sorted arrays without using Extra space.

def find(array1, array2, n1, n2):
    # append array2 to array1
    for i in array2:
        array1.append(i)
    array1 = list(set(sorted(array1)))

    array2 = array1[len(array1) - n2:]
    array1 = array1[:len(array1) - n2]

    print("After")
    print("Array1: ", array1, "\nArray2: ", array2)


array1 = [1, 2, 3, 5, 8, 9, 10, 13, 15, 20]
array2 = [2, 3, 8, 13]

print("Before: ")
print("Array1: ", array1)
print("Array2: ", array2)

find(array1, array2, len(array1), len(array2))