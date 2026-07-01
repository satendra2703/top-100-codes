#A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.

num = int(input("Enter a number: "))
total = 0

for i in range(2 , num):
    if num % i == 0:
        total += i

if total > num:
    print(num, "is an Abundant number")
else:
    print(num, "is not an Abundant number")