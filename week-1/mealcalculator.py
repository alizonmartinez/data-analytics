#Alizon Martinez
# 11/10/2026
# mealcalculator.py

#  Get meal cost from user
meal_cost = float(input("Enter the cost of the meal: $"))

# Calculate tip and tax
tip = meal_cost * 0.20
tax = meal_cost * 0.0825

# Calculate total
total = meal_cost + tip + tax

# Display results
print("\n----- Meal Cost Breakdown -----")
print(f'{"Meal Cost:":<15} ${meal_cost:>6.2f}')
print(f'{"Tip (20%):":<15} ${tip:>6.2f}')
print(f'{"Tax (8.25%):":<15} ${tax:>6.2f}')
print("-" * 30)
print(f'{"Total Cost:":<15} ${total:>6.2f}')

