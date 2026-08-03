#Find if there is any subarray with sum equal to 0 in python ?
"""We will get an array as input from user. We need to find if there is any subarray with sum equal to 0."""
"""Here, in this page we will discuss the program to find if there is any Subarray with sum equal to 0 in Python programming language. If such subarray is present then print True otherwise print False.

Example :

Input :  [ 4, 2, -3, 1, 6 ]
Output :  True
Explanation :  There is a subarray with zero sum from index 1 to 3, { 2+(-3)+1 = 0 }"""

def subArray(arr, l):
    for i in range(l - 1):
        s = arr[i]
        for j in range(i + 1, l):
            s += arr[j]
            if s == 0:
                return True
    return False


array = [4, 2, -3, 1, 6]

print(subArray(array, len(array)))