#Capitalize the first and last character of each word of a string in python ?
"""In this python program, we will be changing the case for the first and last character of the string. Changing case in the string doesn’t only change the look of the string but also changes its value in many ways like it change the ASCII value of the character and also changes its sensitivity because when we perform operations on string case sensitivity of a character changes many things like when you match a lowercase a with uppercase it will give false result."""

#take user input
String = input('Enter the String :')
#start slicing the String
#take 1st character and convert it to upper case
#Concatinate the string with remaning-1 length
#take last character and change it to uppercase and concatinate it to string
String = String[0:1].upper() + String[1:len(String)-1] + String[len(String)-1:len(String)].upper()
#print the String
print(String)