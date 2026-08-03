#Find factorial of a Large Number in python ?
"""We will get a number as input from user. We need to find the factorial of that number."""
"""Factorial of a number is product of all the positive numbers less then and equals to the number we are finding factorial. On this page we will see two different ways to solve the Question one by inbuilt function and another by creating a function.

Input : 5
Output : 120
Explanation : 5! = 5 x 4 x 3 x 2 x 1 = 120"""

def factorial(n):
    ans = 1
    while n > 1:
        ans *= n
        n -= 1

    return ans
n = 5
print(factorial(n))