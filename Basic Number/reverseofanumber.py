num = int(input("Enter a number: "))
temp = num
reverse = 0
while temp > 0:
    reminder = temp % 10
    reverse = (reverse * 10) + reminder
    temp = temp // 10
print("The reverse of the number is:",reverse)