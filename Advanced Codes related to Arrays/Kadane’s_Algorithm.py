#Kadane’s Algorithm  in python ?
"""Kadane’s Algorithm can be viewed both as greedy and DP. As we can see that we are keeping a running sum of integers and when it becomes less than 0, we   reset it to 0 (Greedy Part). This is because continuing with a negative sum is way worse than restarting with a new range. Now it can also be viewed as a DP,   at each stage we have 2 choices: Either take the current element and continue with the previous sum OR restart a new range with the current element. We can keep track of the maximum sum we have seen so far and return it at the end."""

def fun(arr, l):
    max_so_far = max(arr)
    for i in range(l - 1):
        s = arr[i]
        for j in range(i + 1, l):
            s += arr[j]
            if s > max_so_far:
                max_so_far = s
    return max_so_far


array = [-2, -3, 4, -1, -2, 1, 5, -3]

print("Largest contiguous subarray sum is :", fun(array, len(array)))