#Check whether array is subset of another array or not in Python?
""" A subset is defined as a set whose elements are all members of another set. We will input two arrays and check whether the second array is subset of first array and display accordingly"""

def isSubset(arr1 , arr2 , m, n):
    i = 0
    j = 0
    for i in range(n):
        for j in range(m):
            if(arr2[i] ==  arr1[j]):
                break

        if ( j == m):
            return 0
        return 1
    
# Driver code
arr1 = [11, 12, 13, 21, 30, 70]
arr2 = [11, 30, 70, 12]
 
m = len(arr1)
n = len(arr2)

if(isSubset(arr1, arr2, m, n)):
    print("arr2[] is subset of arr1[] ")
else:
    print("arr2[] is not a subset of arr1[]")
    