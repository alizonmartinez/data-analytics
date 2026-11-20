# Alizon Martinez
# 11/10/26
# Syntax for rentals

tourists = 38
seats_per_van = 15

import math

vans_needed = math.ceil(tourists / seats_per_van)

total_cost = vans_needed * 250

cost_per_person = total_cost / tourists

print("Vans needed:", vans_needed)
print("Total cost: $" + format(total_cost, ".2f"))
print("Cost per person: $" + format(cost_per_person, ".2f"))

