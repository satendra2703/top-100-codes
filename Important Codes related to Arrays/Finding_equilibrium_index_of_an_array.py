#Finding equilibrium index of an array in python ?
"""Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes."""

def equilibrium(arr):
    n = len(arr)

    for i in range(n):
        leftsum = 0
        rightsum = 0

        # Left sum
        for j in range(i):
            leftsum += arr[j]

        # Right sum
        for j in range(i + 1, n):
            rightsum += arr[j]

        if leftsum == rightsum:
            return i

    return -1


# Driver code
arr = [-4, 1, 5, 2, -4, 4, 2]
print("Equilibrium index is", equilibrium(arr))
        



    