# Alizon Martinez 
# 11/10/26
# Create syntax for formula 

#√((x2-x1)^2 + (y2-y1)^2)

import math
x1 = 2 
y1 = 3
x2 = 8 
y2 = 10

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("Distance is", round(distance,2))
