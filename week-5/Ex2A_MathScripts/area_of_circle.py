# Alizon Martinez 
# 11/09/26
# Create a script for area of a circle 

# Area = pi x r^2

import math

diameter = 12
radius = diameter / 2

area = math.pi * radius ** 2

print("The area of a circle with radius " + str(radius) + " is " + format(area, ".2f"))

