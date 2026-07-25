#Remove all characters from string except alphabets in python ?
"""We will do this by checking ASCII values of each character present in the string and remove all character that does not lie in the range of alphabetic ASCII value whether it is an uppercase letter or a lowercase letter."""

#take user input
String1 = "#Justice!For@Chutki123"
#initialize empty String
String2 = ''
for i in String1:
    #check for alphabets
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        #concatenate to empty string
        String2+=i
print('Alphabets in string are :' + String2)