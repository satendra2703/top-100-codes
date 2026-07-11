#Calculate Length of the String using Recursion in Python ?
"""That the given program counts any spaces present in string. For example, length of “Hi” is 2 but length of ” Hi” or “Hi ” is 3."""

def length(str):
    if str == "":
        return 0
    else:
        return 1 + length(str[1:])
    
str = input("Enter a string : ")
print("Length of the string is:", length(str))