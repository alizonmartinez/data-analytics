# Alizon Martinez
# 11/13/26
# If/Else statements

purchase_amount = float(input("Purchase amount: "))

if purchase_amount >= 100:
    shipping = 0

else:
    shipping = 9.99

print(f"Shipping cost: ${shipping:.2f}")
