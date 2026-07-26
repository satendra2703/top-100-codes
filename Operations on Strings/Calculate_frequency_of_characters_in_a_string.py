#Calculate frequency of characters in a string in python ?
"""In this python program, we will be  Calculating the Frequency of a character in a string or how many times a character is present in a string.

The string is a datatype in programing language and is formed when 2 or more characters join or concatenate together. Now it is not necessary for a string to have a distinct character, it can be meaningless or meaningful can have distinct characters or can be a combination of the same characters."""

string = "Yolo Life"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")