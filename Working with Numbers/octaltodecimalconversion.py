#Here, in this page we will discuss the program for octal to decimal conversion in python . Octal numbers are also called numbers with base 8 and hold values from 0 – 7. Whereas in Decimal numbers are with base 10 is Standard number system for denoting integers and non-integers. 

def octaltodecimal(num):
    decimal_value = 0
    base = 1

    while num :
        last_digit = num % 10
        num = int(num / 10)
        decimal_value += last_digit * base
        base *= 8
    return decimal_value

octal_num = int(input("Enter an octal number:"))
print("The decimal equivalent of octal", octal_num, "is", octaltodecimal(octal_num))
