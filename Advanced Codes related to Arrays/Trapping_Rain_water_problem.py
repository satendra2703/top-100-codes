#Trapping Rain water problem in python ?
"""We are given with n non-negative integers representing an elevation map where the width of each bar is 1, we need to compute how much water it is able to trap after raining.

Example :

Input : arr = [2,0,3,0,2,0,4]
Output : 9
Explanation : We can trap “2 units” of water between 2 and 3, “7 units” between 3 and 4 (“3 units” between 3 and 2 , “1 unit” on top of bar 2 and “3 units” between 2 and 4."""

def rain(arr):
    ans = 0
    temp = 0
    prev = 0
    for i in range(len(arr)):
        if arr[i] > prev and temp == 0:
            prev = arr[i]
        elif arr[i] >= prev:
            ans += temp
            prev = arr[i]
            temp = 0
        else:
            if i != len(arr)-1 and arr[i] < max(arr[i+1:]):
                temp += prev - arr[i]
            else:
                ans += arr[i]
                temp = 0
                prev = arr[i]
    return ans


arr = [2, 0, 3, 0, 2, 0, 4]
print(rain(arr))