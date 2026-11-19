item1 = 25.75
item2 = 45.67
item3 = 45.75
item4 = 55.67
item5 = 45.60

sales_tax_rate = 0.07

subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * sales_tax_rate
total_cost = subtotal + tax

print(f"Sub-Total = {subtotal:.2f}")
print(f"      Tax = {tax:.2f}")
print(f"Total Cost = {total_cost:.2f}")
