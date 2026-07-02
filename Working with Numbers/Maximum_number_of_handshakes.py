#Maximum Number Of Handshakes in Python
"""For the number of handshakes to be maximum, every person should handshake with every other person in the room i.e. all persons present should shake hands."""

# no. of people in the room
n = int(input("Enter the number of people in the room :"))

# formula to calculate maximum number of handshakes
no_of_handshakes = (n * (n - 1)) // 2
print("The maximum number of handshakes that can take place in the room is :", no_of_handshakes)