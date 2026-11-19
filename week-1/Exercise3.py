# Prompt the user to enter an employee name and performance score
name = input("Enter employee name: ")
score = int(input("Enter performance score:"))

# Use if, elif, snd else statements to determine the employee's rating
if score >= 90:
    rating = "Outstanding"
elif score >= 80:
    rating = "Exceeds Expectations"
elif score >= 70:
    rating = "Meets Expectations"   
elif score >= 60:
    rating = "Below Expectations"
else:
    rating = "Unsatisfactory"

# Display