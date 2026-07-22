#Length of the string without using strlen() function  in python ?
"""Every datatype that stores some value have some length and length of a variable only can be calculated if its datatype can be iterated just like String can be iterated but Integer datatypes are not iterated. One way to find the length of String is by using in-built function len() and the other is by iterating through the string and incrementing the counter by one till loop ends."""

#take user input
string = 'Hello'

count = 0

for i in string:
 
    count+=1
print(count)