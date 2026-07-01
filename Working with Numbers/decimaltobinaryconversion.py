#A decimal number is a standard representation of integers or non-integers, decimal numbers are also called as numbers with base 10. Whereas in binary number system numbers are with base 10 and shows representation by 0 and 1.

def convertbinary(num):
    binary_array = []
    while num > 0:
        binary_array.append(num % 2)
        num = num // 2
    for j in binary_array :
        print(j,end="")

decimal_num = int(input("Enter a decimal number: "))
convertbinary(decimal_num)