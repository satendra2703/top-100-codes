#Minimum no. of Jumps to reach the end of an array in python ?
""" If not possible print -1.

Example:-

Input: arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
Output: 3 (1-> 3 -> 9 -> 9)
Explanation: Jump from 1st element to 2nd element as there is only 1 step, now there are three options 5, 8 or 9. If 8 or 9 is chosen then the end node 9 can be reached. So 3 jumps are required."""

def jump(arr):
    ans = 0
    i = 0
    while i < len(arr) - 1:
        if i + arr[i] < len(arr):
            ans += 1
            if arr[i] == 1:
                i += arr[i]
            else:
                i += arr.index(max(arr[i + 1:arr[i] + i + 1])) - i
        else:
            ans += 1
            i += arr[i]

    return ans


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print("Minimum no of jumps required to reach end of the array : ", jump(arr))