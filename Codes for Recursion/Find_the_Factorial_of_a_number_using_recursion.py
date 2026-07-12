#Find the Factorial of the Number using Recursion in Python?

def factorial(n):
    if n == 0 :
        return 1
    return n * factorial( n - 1)

num = int(input("enter the number : "))
print("factorial of", num , "is", factorial(num) )

