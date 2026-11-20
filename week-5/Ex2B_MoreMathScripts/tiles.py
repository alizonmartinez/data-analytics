# Alizon Martinez
# 11/10/26
# Syntax: Formula for area

import math

length = 12
width = 10

room_area = length * width

tiles_needed = room_area * 1.10

boxes_needed = math.ceil(tiles_needed / 12)

print("Room area:", room_area)
print("Boxes needed:", boxes_needed)