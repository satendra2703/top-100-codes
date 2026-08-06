#Minimum no. of operations required to make an array palindrome in python ?
"""We are given an array of integers, we need to find the minimum number of operations required to make the array palindrome. In one operation, we can merge two adjacent elements.
Example :

Input : array = [2, 10, 12, 26, 3, 22, 2]
Output : 2
Explanation : We need to merge 10 and 22 so, the array will become [2, 22, 26, 3, 22, 2]. Again we will merge 26 and 3 so the array becomes [2, 22, 29, 22, 2]. Now, the array becomes palindromic, hence we need to do 2 merging operations to make the given array palindromic."""

def find(arr):
    ans = 0

    i, j = len(arr) - 1, 0
    while j <= i:
        if arr[j] == arr[i]:
            j += 1
            i -= 1

        elif arr[j] > arr[i]:
            i -= 1
            arr[i] += arr[i + 1]
            ans += 1

        else:
            j += 1
            arr[j] += arr[j - 1]
            ans += 1

    return ans


array = [2, 10, 12, 26, 3, 22, 2]
print("Total number of merging operation required is", find(array))