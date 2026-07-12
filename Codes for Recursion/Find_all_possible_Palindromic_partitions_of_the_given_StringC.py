#Find all possible Palindromic Partitions of the given String in Python?

def isPalindrome(str, low, high):
    while low < high:
        if str[low] != str[high]:
            return False
        low += 1
        high -= 1
    return True

def allpalpartUtil(allpart, currpart, start, n, str):
    
    if start >= n:
        x = currpart.copy()
        allpart.append(x)
        return
    
    for i in range(start, n):
        if isPalindrome(str, start, i):
            currpart.append(str[start: i + 1])
            allpalpartUtil(allpart, currpart, i + 1 , n, str )
            currpart.pop(-1)

def allPalPartitions(str):
    n = len(str)
    allpart = []
    currpart = []
    allpalpartUtil(allpart, currpart, 0, n, str)

    for i in range(len(allpart)):
        for j in range(len(allpart[i])):
            print(allpart[i][j], end = " ")
        print()

string = "sattu"
allPalPartitions(string)
