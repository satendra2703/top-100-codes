num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
"""print("Prime numbers between", num1, "and", num2, "are:")
for num in range(num1, num2 + 1):           
    if num > 1:                               
        for i in range(2, num):              
            if (num % i) == 0:               
                break
        else:
            print(num)"""

prime = []
for i in range(num1,num2+1):
    flag = 0
    if i < 2 :
        continue
    if i == 2:
        prime.append(2)
        continue

    for x in range(2,i):
        if i % x == 0:
            flag = 1
            break
        
        if flag ==0:
            prime.append(i)

print(prime)
