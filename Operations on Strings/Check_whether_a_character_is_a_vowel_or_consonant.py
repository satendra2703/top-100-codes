#Check whether a character is a vowel or consonant in python ?
"""In Python string is an array representation of Characters python does not have a character data type. A single character is a string of length [1].
Vowels:- A character is considered as a vowel when it belongs to the set of characters like { ‘A’ , ‘E’ , ‘I’ , ‘O’ , ‘U’ }"""

c = 'a'

# checking for vowels
if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
    print(c, "is a vowel")  # condition true input is vowel
else:
    print(c, "is a consonant")  # condition true input is consonant