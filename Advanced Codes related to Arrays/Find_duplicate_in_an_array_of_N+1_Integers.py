#Find duplicate in an array of N+1 Integers in python ?

def findDuplicate(arr):
    seen = set()

    for num in arr:
        if num in seen:
            return num
        seen.add(num)

    return -1


# Driver Code
arr = [1, 3, 4, 2, 2]

print("Duplicate element is:", findDuplicate(arr))