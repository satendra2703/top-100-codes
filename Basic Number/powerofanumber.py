num = int(input("Enter a number: "))
power = int(input("Enter the power: "))

#print(pow(num, power))

output = 1
for i in range(power):
    output *= num
print(output)