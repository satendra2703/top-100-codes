#Chocolate Distribution problem – C in python ?
"""We are given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that:
1. Each student gets exactly one packet."""

def minDiff(arr, m, l):
    ans = 1000
    arr.sort()
    for i in range(l - (m - 1)):
        if arr[i + m - 1] - arr[i] < ans:
            ans = arr[i + m - 1] - arr[i]
    return ans


arr = [12, 4, 7, 9, 2, 23, 25]
m = 4
l = len(arr)
print(minDiff(arr, m, l))