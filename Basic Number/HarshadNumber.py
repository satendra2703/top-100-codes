#A Number that is divisible by the sum of it's digits is known as a Harshad number.
num = int(input("Enter a number: "))
temp = num
sum_of_digits = 0
while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    temp //= 10
if num % sum_of_digits == 0:
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")
    