# Prompt the user 
name = input("Enter employee name: ")
salary = float(input("Enter employee salary: $"))
bonus_percentage = float(input("Enter bonus percentage: "))
bonus = salary * bonus_percentage / 100
total_compensation = salary + bonus
print(f"Employee Name: {name}")
print(f"Salary: ${salary:.2f}")
print(f"Bonus: ${bonus:.2f}")
print(f"Total Compensation: ${total_compensation:.2f}")