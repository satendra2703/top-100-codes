#Check whether a character is a alphabet or not in python ?
""".All characters whether alphabet, digit or special character have ASCII value. Input character from the user will determine if it’s Alphabet, Number or Special character."""

# Python Program to find character is alphabet or not

# user input
ch = 'z'

# basic logic
if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print("The  character", ch, "is an Alphabet")
else:
    print("The  character", ch, "is not an Alphabet")