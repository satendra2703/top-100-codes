#Roots of a quadratic equation in Python ?
"""The roots of a quadratic equation are the values of x that satisfy the equation ax^2 + bx + c = 0. The roots can be real or complex, and they can be found using the quadratic formula: x = (-b ± √(b^2 - 4ac)) / (2a)."""

# Write a program to find roots of a quadratic equation in Python
import math
 
def findRoots(a, b, c):
 
    if a == 0:
        print("Invalid")
        return -1
        
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))
 
    if d > 0:
        print("Roots are real and different ")
        print((-b + sqrt_val)/(2 * a))
        print((-b - sqrt_val)/(2 * a))
    elif d == 0:
        print("Roots are real and same")
        print(-b / (2*a))
    else:  # d<0
        print("Roots are complex")
        print(- b / (2*a), " + i", sqrt_val)
        print(- b / (2*a), " - i", sqrt_val)
 
 
# Driver Program
a = 1
b = 4
c = 4
 
# Function call
findRoots(a, b, c)