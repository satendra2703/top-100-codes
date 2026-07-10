#LCM of a Number using Recursion in Python
"""LCM – Lowest common multiple of two or more number. Is Smallest number that it is completely divisible by all the numbers for which we are finding LCM"""

def lcm(a, b, multiple=None):
    if multiple is None:
        multiple = max(a, b)

    if multiple % a == 0 and multiple % b == 0:
        return multiple

    return lcm(a, b, multiple + max(a, b))

# Example
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM =", lcm(num1, num2))