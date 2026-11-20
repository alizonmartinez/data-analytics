# Alizon Martinez
# 11/19/26
# Create classes

class Restaurant:
    """
    Stores information about a restaurant.
    """

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

# Objects

rest1 = Restaurant("Olive Garden", "Italian food")

rest2 = Restaurant("Red Lobster", "Seafood")

rest3 = Restaurant("Cafe Rio", "Mexican food")

rest1.describe_rest()
rest1.rest_open()

print()

rest2.describe_rest()
rest2.rest_open()

print()

rest3.describe_rest()
rest3.rest_open()



