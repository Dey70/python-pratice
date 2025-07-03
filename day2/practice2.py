print("Tip Calculator Project")

bill = float(input("Enter the amount of bill?: "))
split = float(input("Enter the number of people you want to split?: "))
tip_percent = float(input("Enter the tip percentage you'd like to give (e.g., 12 for 12%): "))

# Convert tip percentage to multiplier
tip_multiplier = 1 + (tip_percent / 100)

# Calculate total per person
total_bill = (bill / split) * tip_multiplier

# Format to 2 decimal places
final_amount = "{:.2f}".format(total_bill)

print(f"Each person should pay: ${final_amount}")
