#Reversing a Number using Recursion in Python ?
"""Note : That the given program doesn’t consider leading zeroes. For example, for 100 program will print 1. If you want to print 001 then remove the int from print statement."""

def reverse_digit(arr, l , n=0):
    if n == l:
        return arr 
    arr[n], arr[-1*(n+1)] = arr[-1*(n+1)], arr[n]
    return reverse_digit(arr, l, n + 1)

num = int(input("enter the number:"))
arr = list(str(num))
arr = reverse_digit(arr, len(arr)//2)
s = ""
print(int(s.join(arr)))
