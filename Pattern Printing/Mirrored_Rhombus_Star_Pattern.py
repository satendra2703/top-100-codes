#Mirrored Rhombus Star Pattern in python ?

n = int(input("Enter the number: "))

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print("  ", end="")

    # Print stars
    for j in range(n):
        print("* ", end="")

    print()