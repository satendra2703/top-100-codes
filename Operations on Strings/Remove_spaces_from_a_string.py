#Remove spaces from a string in python ?
"""Here we will write python program, we will Remove spaces from a string words whether the sentence is meaningful or meaningless and we can do this in two different ways:-

By traversing the string and removing spaces.
Using the join function."""

#take user input 
String = "PrepInsta is fabulous"

#Use join function 
String = "".join(String.split()) 

#print String 
print("After removing spaces string is :",String)