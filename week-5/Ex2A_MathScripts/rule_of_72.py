# Alizon Martinez
# 11/09/26
# Create a script for Rule of 72

# Years to Double = 72/Interest Rate

current_savings = 5000
interest_rate = 0.06

years = 72 / 6
future_value = current_savings * 2

print("Your current savings is " + format(current_savings, ".2f"))
print("At a " + format(interest_rate, ".0%") + " interest rate,")
print("your savings account will be worth " + format(future_value, ".2f"))
print("in " + format(years, ".1f") + " years")

