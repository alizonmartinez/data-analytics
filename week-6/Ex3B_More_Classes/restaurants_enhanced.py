# Alizon Martinez
# 11/18/26
# Created classes

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

def __init__(self, rest_name, food_type):
    self.rest_name = rest_name
    self.food_type = food_type

    self.number_served = 0
    self.customer_ratings = []

def add_num_served(self):

    customers = int(input("How many customers served today? "))

    self.number_served += customers

def print_num_served(self):

    print(
        f"{self.rest_name} has served {self.number_served} customers."
    )

def customer_rating(self):

    rating = int(
        input(
            "How would you rate your experience today on a scale of 1-5? "
        )
    )

    self.customer_ratings.append(rating)

    average = sum(self.customer_ratings) / len(self.customer_ratings)

    print(
        f"Your rating was {rating}. "
        f"The average rating for this restaurant is {average:.2f}"
    )

rest1 = Restaurant("Olive Garden", "Italian")

rest2 = Restaurant("Cafe Rio", "Mexican")

rest3 = Restaurant("Texas Roadhouse", "Steakhouse")

rest1.print_num_served()

rest1.add_num_served()

rest1.add_num_served()

rest1.print_num_served()

rest1.customer_rating()

rest1.customer_rating()

rest1.customer_rating()

def customer_rating(self):

    while True:

        try:

            rating = int(
                input(
                    "How would you rate your experience today on a scale of 1-5? "
                )
            )

            if rating < 1 or rating > 5:

                print("Rating must be between 1 and 5.")
                continue

            self.customer_ratings.append(rating)

            average = (
                sum(self.customer_ratings)
                / len(self.customer_ratings)
            )

            print(
                f"Your rating was {rating}. "
                f"The average rating is {average:.2f}"
            )

            break

        except ValueError:

            print(
                "Please enter a whole number between 1 and 5."
            )

