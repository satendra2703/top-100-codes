#N-bit binary numbers having more  or equal 1’s than 0’s in Python?

def printRec(number, extraOnes, remainingPlaces):
    if 0 == remainingPlaces:
        print(number, end=" ")
        return
    
    printRec( number + "1", extraOnes + 1, remainingPlaces - 1)

    if extraOnes > 0:
        printRec( number + "0", extraOnes - 1, remainingPlaces - 1)

def printNums(n):
    str = ""
    printRec(str, 0 , n)

n = int(input("Enter the number of bits : "))
print("The N-bit binary numbers having more or equal 1’s than 0’s are : ")
printNums(n)
    