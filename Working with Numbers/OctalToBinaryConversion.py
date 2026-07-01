#Numbers with base 8 are called octal numbers and uses digits from 0-7 for representation of octal number. Where as numbers with base 2 are called binary numbers  and it uses 0 and 1 for representation of binary numbers.

def convert(octal):
    i = 0
    decimal = 0
    while octal != 0:
        digit = octal % 10
        decimal += digit * pow(8, i)
        octal //= 10
        i += 1
    print("Decimal Value :", decimal)
    binary = 0
    rem = 0
    i = 1

    while decimal != 0:
        rem = decimal % 2
        decimal //= 2
        binary += rem * i
        i *= 10
    print("Binary Value :", binary)


octal = int(input("Octal Value : "))
convert(octal)