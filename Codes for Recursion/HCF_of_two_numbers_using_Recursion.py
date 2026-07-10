#HCF of a Number Using Recursion in Python ?
"""HCF – Highest common factor of two or more number such that it can completely divide all the numbers."""

def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


first = 23
second = 69

print('HCF of', first, 'and', second, 'is', hcf(first, second))