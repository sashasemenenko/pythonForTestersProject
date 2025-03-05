# Create a function called 'calculate average' that takes one argument 'numbers', which is a list of integers
def calcullate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

numbers = [3, 4, 6]

result = calcullate_average(numbers)
print(f"The average of the numbers is: {result:.2f}")
