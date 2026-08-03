#Find all pairs on integer array whose sum is equal to given number in python ?
"""We will get an array as input from user. We need to find all possible pairs from the given array whose sum is same as given sum. 

Example:

Array :   [5, 2, 3, 4, 1, 6, 7]
Sum= 7
Possible pairs:  [5, 2], [3, 4], [1, 6]"""

def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


array = [5, 2, 3, 4, 1, 6, 7]

# Take sum as input from user
summ = 7

# print array
print("Array= ", array)

# call function find
find(array, len(array), summ)