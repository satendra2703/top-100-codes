#Toggle each character in a string in python ?
"""The string is a combination of characters, but in programing language like python, a string is an independent datatype that can be treated as character or string both because in python string of length 1 is also a string, not character. In this python program, we will check the type of string available on the basis of their case

So Today we will se program to Toggle each character in a string"""

#take user input
String = 'GuDDuBHaiyA'
#initialize other empty String
String1 = str()
#iterate through String
for i in String:
    #check the case of each iterator
    if i.isupper():
        #change it to opposit case
        i = i.lower()
        #Concat each iterator to String1
        String1 = String1 + i
    else:
        i = i.upper()
        String1 = String1 + i
#print String1
print(String + ' after changing ' + String1)