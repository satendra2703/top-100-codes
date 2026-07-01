num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
hcf = 1 

for i in range(1, min(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print("The HCF of", num1, "and", num2, "is", hcf)