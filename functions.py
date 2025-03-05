from booleans import result
from loops import total


def hello_world():
    print("Hello, World!")


hello_world()


def greet(name, age):
    print(f"Hello {name}, you are {age} years old.")


greet("Oleksandr", 37)


# Allow to input any numbers to the functions
def sum_numbers(*numbers):
    total = 0
    for number in numbers:
        total += number
    print(total)


sum_numbers(3, 2.4, 45, 67)


def dispay_info(name, age, city="Unknown"):
    print(f"Nema: {name}, age: {age}, city: {city}")


dispay_info("Oleksandr", 38)
dispay_info(name="Nadiia", age=38, city="Warsaw")


def display_fruits(fruits_list):
    for fruit in fruits_list:
        print(fruit)


my_fruits = ['apple', "banana", "cherry"]

display_fruits(my_fruits)


def multiply(a, b):
    result = a * b
    return result

result = multiply(5, 4)
print(result)

def calculate(a, b):
    sum = a + b
    diff = a - b
    return sum, diff

result_sum, result_diff = calculate(7, 3)
print(f"Sum: {result_sum}, Diff: {result_diff}")
