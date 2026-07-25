#Remove brackets from an algebraic expression in python ?
"""In an algebraic expression, brackets show the priority of the operation. If the operator outside the bracket has more precedence than the operator between the operands in the brackets the operation inside the brackets will be performed first and then the output of the operation will be operated with operand outside the brackets."""

#take user input
Exp = "(a-b)+[c*d]+{e/f}"
#initialize an empty string 
Equation = ''
#traversing through string
for i in Exp:
    #checking for brackets
    if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
        #If True
        pass
    else:
        #if False
        #add it to empty String
        Equation = Equation + i
 #print the string
print(' String without bracket is ' + Equation)
