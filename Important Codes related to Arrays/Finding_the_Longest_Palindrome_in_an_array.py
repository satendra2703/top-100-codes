#Find the Longest Palindrome in an Array using Python ?

#function to check if n is Palindrome
def isPalindrome(n):
   
    devisior = 1
    while  (int(n / devisior) >= 10):
        devisior *= 10

    while (n != 0):
        leading = int(n / devisior)
        trailing = n % 10

        if (leading != trailing):
            return False
        
        n = int(( n % devisior)) / 10

        devisior = int (devisior / 100)
    return True

#function to find the largest palindromic element
def largestPalindrome(arr, n):
    currentMax = -1

    for i in range(0, n , 1 ):
        if (arr[i] > currentMax and isPalindrome(arr[i])):
            currentMax = arr[i]

    return currentMax

#Driver Code
arr = [1, 232, 5545455, 909090, 161]
n = len(arr)

# print required answer
print(largestPalindrome(arr, n))
