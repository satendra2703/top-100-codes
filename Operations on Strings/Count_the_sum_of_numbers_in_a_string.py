#Count the sum of numbers in a string in python ?
"""Here we will use alphanumeric strings to find the sum of all numbers in that string basically well Count the sum of numbers in a string.Numbers can be added, but strings follow the rule of concatenation a string of alphabets will be concatenated before or after one another but in case of integers, numbers are added to each other to form a new number. Strings can be of many types:-
 
AlphaNumeric
Numeric
Character"""

#take user input
String = "Daya123Ben456"
#initialize integer variable
sum1 = 0
for i in String:
    #check if values lies between range of numbers or not
    #according to ascii tale
    if ord(i) >= 48 and ord(i) <= 57:
        #convert it to integer and add
        sum1 = sum1 + int(i)
print('Sum is :' + str(sum1))