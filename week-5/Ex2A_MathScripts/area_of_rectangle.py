# Alizon Martinez
# 11/09/26
# Create script for area of a rectangle 

#Use birthday as side length and width
# Janurary 16

side_a = 1
side_b = 16

area = side_a * side_b

print("Side A is " + str(side_a))
print("Side B is " + str(side_b))
print("The area of the rectangle is " + str(area))

# Use input ()

side_a = float(input("What is the first side? "))
side_b = float(input("What is the second side? "))

print("Area =", area)

# Input is retured as text.
# Numbers must often be converted using int () or \
# float () for decimals.
# Users may type inviald values and cause errors.

# Rewrite as f-strings

print(f"Side A is {side_a}")
print(f"Side B is {side_b}")
print(f"The area is {area}")

