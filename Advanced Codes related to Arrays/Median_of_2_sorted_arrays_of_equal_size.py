#Median of 2 sorted arrays of equal size in python ?
"""We are given two arrays say arr1[ ] and arr2[ ] of the same size say n. We need to find the median after merging these arrays.

Example :

Input : arr1 = [ 1, 12, 15, 26, 38 ],  arr2 = [ 2, 13, 17, 30, 45 ]
Output : 16
Explanation : After merging and sorting the array it will be [ 1, 2, 12, 13, 15, 17, 26, 30, 38, 45 ], middle elements are 15 and 17 so, median of the given array will be ((15+17)/2) = 16"""


from math import ceil


def median_of_two_arrays(l, array):
    if (l % 2) == 0:
        medium = l // 2
        median = (array[medium] + array[medium - 1]) / 2
        return median
    else:
        medium = ceil(l / 2)
        return array[medium - 1]


array1 = [1, 12, 15, 26, 38]
array2 = [2, 13, 17, 30, 45]

print("Array after merging and sorting :", end="")
array1 += array2
array1.sort()
print(array1)
ans = median_of_two_arrays(len(array1), array1)
print("Median :", int(ans))