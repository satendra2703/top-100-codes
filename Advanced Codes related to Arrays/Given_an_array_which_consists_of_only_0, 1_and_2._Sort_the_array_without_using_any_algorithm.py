#Given an array which consists of only 0, 1 and 2. Sort the array without using any  algorithm in python ?
"""In this article we will see a Python Program to sort the given array which consist of 0,1,2. User will enter elements of array which is either 0,1 or 2. We have to sort that array consisting o,1 and 2 but without using sorting algorithm. We will use count function to count different elements and then arrange them.

Example:-

Array: 1 2 0 2 1 0 2 1 0 2 0 1
Array after sorting: 0 0 0 0 1 1 1 1 2 2 2 2"""

def sort(arr):
     # Note: We cannot use sort function
    # we will find the count of 0,1,2 in the given array with help of count function
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    count_2 = arr.count(2)

    # declare new array
    new_arr = []

    # append 0 to new array
    for i in range(count_0):
        new_arr.append(0)

    for i in range(count_1):
        new_arr.append(1)

    for i in range(count_2):
        new_arr.append(2)

    print(" After sorting:", new_arr)


array = [1, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1]
print("Before Sorting:", array)
# call function
sort(array)