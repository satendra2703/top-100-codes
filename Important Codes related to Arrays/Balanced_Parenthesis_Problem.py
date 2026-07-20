#Balanced Parenthesis Problem in python ?
""" To do this , the traditional way of doing is using stacks but we can also find by using normal programming techniques. Different brackets are  ( ) , [ ] , { }. Question can be asked on any type of bracket or of all types of brackets."""

def isbalanced(s):
  c= 0
  ans=False
  for i in s:
    if i == "(": 
     c += 1
    elif i == ")":
     c-= 1
    if c < 0:
     return ans
    if c==0:
     return not ans
  return ans
s="{[]}"
print("Given string is balanced :",isbalanced(s))