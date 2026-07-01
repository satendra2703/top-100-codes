#Decimal numbers are the standard representation for representing integer or non-integer values. Decimal numbers are with base 10 and can represent numbers from 0-9. Whereas in Octal representation of numbers, numbers from 0-7 are represented as octal numbers are with base 8.

decimal = int(input("Enter a decimal number: "))
octal = []
while decimal > 0:
    r = decimal % 8
    octal.append(r)
    decimal = decimal // 8

# Print the octal number in reverse order
for i in reversed(octal):
    print(i, end="")