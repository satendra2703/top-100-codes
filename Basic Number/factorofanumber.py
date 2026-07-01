def printdivisors(n):
    i = 1 
    while i <= n:
        if n % i == 0:
            print(i,end =" ")
        i = i + 1

print("the divisor of the number is:")
printdivisors(int(input("Enter a number: ")))
