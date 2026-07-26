#Check if two strings match where one string contains wildcard characters in python ?
"""In this program, we will make a function solve() with boolean as a return type, that will return true if the strings match else it will return false. Then we will check whether function returns True or false and prints the respective message to output."""

def solve(a,b):
    n,m=len(a),len(b)
    if n==0 and m==0:
        return True
    if n > 1 and a[0] == '*' and m == 0:
        return False
    if (n > 1 and a[0] == '?') or (n != 0 and m !=0 and a[0] == b[0]):
        return solve(a[1:],b[1:]);
    if n !=0 and a[0] == '*':
        return solve(a[1:],b) or solve(a,b[1:])
    return False

str1="Prepins*a"
str2="Prepinsta"
print("First string with wild characters :" , str1)
print("Second string without wild characters ::" , str2)
print(solve(str1,str2))