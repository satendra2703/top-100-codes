#Check if the given string is Palindrome or not in python ?
"""A palindrome is a word, phrase, or sequence that reads the same backwards as forwards. They can be both numeric and characters. For instance – 

Example
Radar, Kayak, 12321,1221

All above are examples of palindrome as they are same when read forwards/backwards"""

# Write a program to check whether a string is palindrome or not in python
input_string = 'civic'
rev = input_string[::-1]

if input_string == rev:
    print(rev + " is Palindrome")
else:
    print(rev + " is not Palindrome")