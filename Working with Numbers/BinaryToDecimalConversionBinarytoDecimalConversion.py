num = int(input("Enter a number: "))
binary_val = num
decimal_val = 0
base = 1

while num > 0:
    rem = num % 10
    decimal_val += rem * base
    base *= 2
    num //= 10

print("The decimal equivalent of binary", binary_val, "is", decimal_val)
