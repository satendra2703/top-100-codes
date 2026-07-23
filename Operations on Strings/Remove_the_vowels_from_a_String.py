#Remove the vowels from a String in python ?
"""The string is built with 2 different types of alphabets grouped as vowels and consonants. In this python program, we will be searching for each alphabet that belongs to the group of vowels and will delete it and print the strings with remaining consonants. As we know String is un-mutable in python so we will initialize a new string and concatenate alphabets that don’t belong to the group of vowels and print it."""

string = "PrepInsta"

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print("\nAfter removing Vowels: ", result)