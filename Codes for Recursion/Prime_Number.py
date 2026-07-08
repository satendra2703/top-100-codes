#Prime Number using Recursion in Python?
"""Prime Number : is a number who is completely divisible by 1 and itself only. """

def prime_number(num, i=2):
    if num == i:
        return True 
    elif num % i == 0:
        return False
    return prime_number(num, i + 1)

num = int(input("enter the number:"))
if prime_number(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

    