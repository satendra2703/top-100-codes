num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == 0 and i % num2 == 0:
        lcm = i
        break

print("The LCM of", num1, "and", num2, "is", lcm)
