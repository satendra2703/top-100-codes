num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

for n in range(num1, num2 + 1) :
    order = len(str(n))

    sum = 0
    
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

        if n == sum :
         print(n,"is an Armstrong number")