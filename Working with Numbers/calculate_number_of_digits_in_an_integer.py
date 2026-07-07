#Number of digits in an integer in Python ?
"""The number of digits present in the Integer is the length of the Integer. Every Character or Integer or any other variable or constant either given by the user or predefined has some length."""

def countDigit(n):
    digit = 0
    while n != 0:
        n //= 10
        digit += 1
    return digit
 
 
# Driver Code
n = 78673
print("Number of digits : % d" % (countDigit(n)))