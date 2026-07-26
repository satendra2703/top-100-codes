#Find non-repeating characters in a string in python ?
"""The string is a combination of characters when 2 or more characters join together it forms string whether the formation gives a meaningful or meaningless output. In python programming, we treat a single character also as a string because there is no datatype as a character in python. In this python program, we will find unique elements or non repeating elements of the string."""

#take user input
String = "prepinsta"
for i in String:
    #initialize a count variable
    count = 0
    for j in String:
        #check for repeated characters
        if i == j:
            count+=1
        #if character is found more than 1 time
        #brerak the loop
        if count > 1:
            break
    #print for nonrepeating characters
    if count == 1:
        print(i,end = " ")