""" 
PI = 3.14
radius = float(input("Enter the Radius of a Cylinder : "))
height = float(input("Enter the Height of a Cylinder : "))
area = 2 * PI * radius * height + 2 * PI * radius ** 2
print("The area of a Cylinder is : {0:.2f}".format(area))

"""
import math
def area_of_Cylinder(radius, height):
    area = 2 * math.pi * radius * height + 2 * math.pi * math.pow(radius,2)
    return area
radius = float(input("Enter the Radius of a Cylinder : "))
height = float(input("Enter the Height of a Cylinder : "))
print("The area of a Cylinder is : {0:.2f}".format(area_of_Cylinder(radius, height)))