#Largest Element in an Array using Recursion in Python ?
"""Given an array of integers “A”, the task is to write a Program for Finding the Largest Element in an Array in Python Language using recursion algorithm."""

def findMaxRec(a, n):
    if n == 1:
        return a[0]
    return max(a[n - 1], findMaxRec(a, n - 1))

# Driver code 
if __name__ == "__main__":
    a = [1,4,45,6,-50,10,2]
    n = len(a)
    print("Largest in given array is", findMaxRec(a, n))
