num = int(input("Enter a number: "))

temp = num
total = 0

# Store factorials of digits 0-9
f = [0] * 10
f[0] = 1
f[1] = 1

for i in range(2, 10):
    f[i] = f[i - 1] * i

# Find sum of factorials of digits
while temp > 0:
    r = temp % 10
    temp = temp // 10
    total += f[r]

# Check strong number
if total == num:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")