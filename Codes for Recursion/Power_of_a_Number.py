#Power of a Number using Recursion in Python ?
""" User have to give base and power as input. Power of a number is basically multiplying the base number by itself , power number of time."""

def power(base, exponent):
    if exponent != 0:
        return base * power(base, exponent - 1)
    else:
        return 1
    
base = int(input("Enter the base number:"))
exponent = int(input("Enter the exponent number:"))

print(base, "to the power", exponent, "is", power(base, exponent))
