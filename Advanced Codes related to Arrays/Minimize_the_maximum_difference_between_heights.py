#Minimize the maximum difference between heights in python ?
"""In this we need to either increase or decrease the height of every tower by k (only once) where k > 0. The task is Python Program to Minimize the Maximum Difference between Heights of the longest and the shortest tower after modifications print out this difference.

Input : arr = [2, 16, 9], k = 6
Output : Maximum difference is 5.
Explanation : We change 2 to 8, 16 to 10 and 9 to 15. Maximum difference is 7
(between 8 and 15). We can’t get a lower difference."""

def profit(arr, k):
    n = (min(arr) + max(arr)) // 2
    new = []
    for i in arr:
        if max(arr) - min(arr) < k:
            return max(arr) - min(arr)
        elif i >= n:
            new.append(i - k)
        else:
            new.append(i + k)
    return max(new) - min(new)


array = [2, 9, 16]
K = 6
print("Maximum difference is :", profit(array, K))