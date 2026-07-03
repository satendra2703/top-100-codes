#Replace All 0’s With 1 In A Given Integer using Python
"""The concept is simple, find the digits of the integer. Compare each digit with 0 if the digit is equal to 0 then replace it with 1. Construct the new integer with the replaced digits."""

num1 = int(input("Enter a number: "))
num2 = 0

if num1 == 0:
    num2 = 1

while num1 > 0:
    rem = num1 % 10
    if rem == 0:
        rem = 1
    num2 = (num2 * 10) + rem
    num1 = num1 // 10

num = 0
while num2 > 0:
    rem = num2 % 10
    num = (num * 10) + rem 
    num2 = num2 // 10
print("The number after replacing all 0's with 1's is:", num)