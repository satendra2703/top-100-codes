#How to find area of circle using python ?
""".Area of circle is the number of square units inside the circle , can be calculated using the radius and diameter.The formula for evaluating the area of circle is

Area of circle using radius=   Pi*r*r    ( r is the radius of circle)
Area of circle using diameter=  1/4*Pi*d*d   ( d is the diameter of circle)
 """

from math import pi
radius = float(input("enter the radius of circle:"))
area = pi * radius * radius 
print("The area of circle ", end = " ")
print(area)
