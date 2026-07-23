#count the number of vowels in a string in python ?
"""There are five vowels in English vocabulary, they are – ‘a’, ‘e’, ‘i’, ‘o’, ‘u’.

For Example, in the string prepinsta then in that case then vowesl are 3 (a,e,i)"""

#take user input
String = input('Enter the string :')
count = 0
#to check for less conditions
#keep string in lowercase
String = String.lower()
for i in String:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        #if True
        count+=1
#check if any vowel found
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(count))