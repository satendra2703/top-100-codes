#Find the ASCII value of a character in python ?
"""The machine doesn’t have the capacity to understand languages that humans do, the machine understands binary language and converts everything to binary format."""

"""ASCII stands for American Standard Code for Information Interchange
Which is a binary code used by electronic equipment for electronic communications
A total of 128 characters have been assigned values from 0 – 127
Alphabets (  65 – 90  &  97 – 122  )
Digits (  48 – 57  )
Remaining are Special Character (  !, @, #, $, * …..)"""

# user input
Char = 'z'

# convert Char to Ascii value
Ascii_val = ord(Char)

# print Value
print('The ASCII value of', Char, 'is', Ascii_val)
