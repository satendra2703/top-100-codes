#Smallest Subarray with sum greater than a given value in python ?
"""We are given an unsorted array containing non-negative integers we need to find a continuous sub-array of minimum length whose sum is greater than the given sum

Example :

Input : arr : [ 1, 4, 0, 0, 2, 6, 3 ] & sum = 6
Output : Sub-array with sum greater than 6 will have a size of 2 Elements
Explanation : For the given array. The sub-array from index 4 to 5 will give a sum of 8 (2+6), greater than the value  6, and the smallest subarray with a sum greater than the given sum."""

def sub(arr, x, l):
    ans = l+1
    for i in range(l):
        sum = 0
        for j in range(i, l):
            sum += arr[j]
            if sum > x:
                if (j - i) < ans:
                    ans = j - i
    if ans > l:
        return "NOT POSSIBLE"
    else:
        return ans + 1


arr = [1, 2, 3, 4, 5]
x = 5
l = len(arr)
print("Sub-array with sum greater than", x, "will have a size of", sub(arr, x, l), "Elements for given array")