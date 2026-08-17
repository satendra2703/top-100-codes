#Inverted Pyramid Star Pattern in python ?

n = int(input("Enter the number: "))

for i in range(n):
    # Print spaces
    for j in range(i):
        print(" ", end="")

    # Print stars
    for j in range(2 * (n - i) - 1):
        print("*", end="")

    print()