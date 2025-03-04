# Assign a hardcoded value for the customer's age
customer_age = 45
# Assign a hardcoded value for the time of the day
time_of_the_day = 1600
# Determine the base price of the movie ticket
base_ticket_price = 12.0
if customer_age <= 12:
    discount = 0.5
elif customer_age >= 60:
    discount = 0.3
elif time_of_the_day < 1700:
    discount = 0.2
else:
    discount = 0
# Calculate the final ticket price
final_ticket_price = base_ticket_price * (1 - discount)
# Print the final ticket price
print(f"The final price is {final_ticket_price:.2f}$.")