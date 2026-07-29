#Move all the negative elements to one side of the array in python ?
"""User will give an array as input to user. We are required to move all the negative elements to one side of the array, that is either to left or right. We will see various method to do so in this article. 

Example:

array= [1, 3, -1, 4, -3, -5, -6, 3, 7]
After moving all the elements to left array =[-6, -5, -3, -1, 1, 3, 3, 4, 7]"""

def find(arr):
    # sort array
    arr.sort()

    # print array
    print("Array after moving all the elements to left:", arr)


array = [1, 3, -1, 4, -3, -5, -6, 3, 7]
# call function
find(array)