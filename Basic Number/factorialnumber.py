num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("factorial does not exist for negative numbers")
else:
    for i in range(1 ,num + 1):
        fact = fact * i 
print("the factorial of",num ,"is",fact )
