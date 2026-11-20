# Alizon Martinez
# 11/13/26
# Using if/elif/else statements

age = int(input("Enter your age: "))

if age < 12:
    ticket_price = 5

elif age < 65:
    ticket_price = 10

else:
    ticket_price = 7

print(f"Ticket price is ${ticket_price}")

