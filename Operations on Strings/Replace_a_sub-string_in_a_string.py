#Replace a sub-string in a string in python 
"""we will be asking the user to input a base string, than we will ask for a substring which is to replaced, and finally we will ask for the string which is to be placed on the place of substring and by using replaceAll() we will replace old string with new one."""

string=input("Enter String :\n")
str1=input("Enter substring which has to be replaced :\n")
str2=input("Enter substring with which str1 has to be replaced :\n")
string=string.replace(str1,str2)
print("String after replacement")
print(string)