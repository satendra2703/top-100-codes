#Replace each element of the array by its rank in the array in python 
"""Given an array of distinct integers, we need to replace each element of the array with its rank. The minimum value element will have the highest rank in the Array"""

def changeArr(input1):
 
    newArray = input1.copy()
    newArray.sort()
     
    for i in range(len(input1)):
        for j in range(len(newArray)):
            if input1[i]==newArray[j]:
                input1[i] = j+1;
                break;
    
# Driver Code
arr = [100, 2, 70, 12 , 90]
changeArr(arr)
# Print the array elements
print(arr)