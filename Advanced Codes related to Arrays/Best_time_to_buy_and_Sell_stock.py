#Best time to buy and Sell stock in python ?
"""Example:

Input: [70, 150, 230, 280, 10, 505, 665]
Output: We can make a maximum profit of 655 
Explanation: For the given set of stock prices we can make a maximum profit of 655 by buying the stock on day 4 & selling it on day 6"""

def profit(arr):
    pro = 0
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] - arr[i] > pro:
                pro = arr[j] - arr[i]
    return pro


array = [70, 150, 230, 280, 10, 505, 665]
print("We can make maximum profit of", profit(array))
