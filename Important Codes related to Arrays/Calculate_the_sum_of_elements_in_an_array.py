#Calculate the sum of elements in an array using python ?

arr = [10, 20, 4, 45, 99]
sum = 0

for i in range(len(arr)):
    sum = sum + arr[i]

print("Sum of all the elements in the array is:", sum)