#Check if two strings are Anagram or not in python ?
"""Anagram program in python is when strings share the same no of characters and also the same characters then strings are called anagrams. The rearrangement of similar characters or letters in a string even if they don’t have the same meanings are anagrams. Only one strict rule is followed if we create anagrams of a string ‘count of every character available in the 1st string should be equal to the count of characters in the 2nd string for the same character."""

# Anagram program in python
# take user input
String1 = "Listen"
String2 = "Silent"

String1 = sorted(String1.lower())
String2 = sorted(String2.lower())

print("String1 after sorting: ", String1)
print("String2 after sorting: ", String2)

# check if now strings matches
if String1 == String2:
    print('Strings are anagram')
else:
    print('Strings are not anagram')