#Smallest Element in an Array in Python ?
"""Given an array of integers “A”, the task is to write a Program for Finding the Smallest Element in an Array in Python using recursion algorithm."""

def findMinRec(a, n):
    if n == 1:
        return a[0]
    return min(a[n - 1], findMinRec(a, n - 1))

# Driver code 
if __name__ == "__main__":
    a = [1,4,45,6,-50,10,2]
    n = len(a)
    print("smallest in given array is", findMinRec(a, n))
    