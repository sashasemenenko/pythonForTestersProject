# Assign a hardcoded value for the customer's age
age = 45
# Assign a hardcoded value for the time of the day
daytime_value = 1600
ticket_price = 12.00
# Determine te base price of the movie ticket
if age <= 12:
    discount = 0.5
elif age >= 60:
    discount = 0.3
elif daytime_value < 1700:
    discount = 0.2
else:
    discount = 0
# Calculate the final ticket price
final_price = ticket_price * (1-discount)
# Print the final ticket price
print(f"Your discount is {final_price: .2f}")
