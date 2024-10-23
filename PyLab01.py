# -*- coding: utf-8 -*-
"""

  Program: CSC115/170 Lab 01
 ----------------------------
  Partner 1:  Dylan Regan
  Partner 2: Hunter Prather
  Date: 09/04/2024
      
      
  Tips:
    1. Read the entire Lab PDF so you understand what you need to do
    2. Be sure to comment your code well.  
       Not too much but enough to explain what you are doing.
       In this first lab I will provide some comments for you to follow
    3. Use descriptive variable names
    4. Print two blank lines in the output between each part
    5. Put any import statements at the top of the code.  
       In this first lab, I provide you with the import statement
      
"""

# Put any import statements here
import math



############################################################
# Part 1 - Area of a Rectangle
############################################################
print( "Part 1: Area of a Rectangle" )

# get the radius and height
length = eval(input("Please enter the rectangle length: "))
width = eval(input("Please enter the rectangle width: "))



# calculate the area
rect_area = length * width


# display result
print("The area of a rectangle with length", str(length), "and length", str(width), "is:", str(rect_area))


# print two blank lines
print("\n")


############################################################
# Part 2 - Surface Area of a Cylinder
############################################################
print( "Part 2: Surface Area of a Cylinder" )

# get the radius and height
radius = eval(input("Please enter the Cylinder radius: "))
height = eval(input("Please enter the Cylinder height: "))


# calculate surface area
cyl_area = (2 * math.pi) * radius * (radius + height)


# display result
print("The surface area of a cylinder with radius", str(radius), "and height", str(height), "is:", str(cyl_area))


# print two blank lines
print("\n")


############################################################
# Part 3 - Volume of a Cone
############################################################
print( "Part 3: Volume of a Cone" )

# get the radius and height
cone_radius = eval(input("Please enter the Cone radius: "))
cone_height = eval(input("Please enter the Cone height: "))


# calculate volume
volume = (math.pi * pow(cone_radius,2) * cone_height)/3


# display result
print("The volume  of a cone with radius", str(cone_radius), "and height", str(cone_height), "is:", str(volume))

