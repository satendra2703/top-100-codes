#as the square of the number ends with the number itself, It's an Automorphic number.

num = int(input("Enter a number: "))
square =pow( num , 2)
mod = pow(10 , len(str(num)))

if square % mod == num:
    print(num,"is an Automorphic number")
else: 
    print(num,"is not an Automorphic number")