# Conditional Statement

age: int = int(input("How old are you? "))

if age > 16:
    print("You are of age!")
    print("Here is a copy of GTA6 for you.")
else:
    print("Denied Access...")
    print("Next costumer, please!")

# Comparison operators
number = int(input("Please type a number: "))

if number < 0:
    print("The number is negative.")
elif number > 0:
    print("The number is positive.")
elif number == 0:
    print(print("The number is zero."))

# Exercise
"""
Write a program and check if a student can pass to next class
"""

name: str = input("Enter your name: ")
mean: float = float(input("Enter your class mean/20: "))

if mean < 0:
    print("You entered a negative value!")
elif mean < 10:
    print(f"😥😥 Sorry {name}!")
    print("Your mean is too low for next class.")
elif mean <= 20:
    print(f"✨✨ Congratulations {name}!")
    print("You pass to next class.")
else:
    print("⛔ Mean must be lower or equal to 20.")

"""
Write a program which asks the user for an integer number.
The program should print out "Orwell" if the number is exactly 1984, and otherwise dot nothing.
"""

entry_number = int(input("Please type the number: "))

if entry_number == 1984:
    print("Orwell")

"""
The Absolute Value
"""
print("---- THE ABSOLUTE VALUE ----")
user_entry = int(input("Please type in a number: "))

if user_entry < 0:
    print(f"Absolute value: {-1 * user_entry}")
else:
    print(f"Absolute value: {user_entry}")

"""
Soup or no soup
"""

username = input("Please tell me your name: ")
portion_price = 5.90

if username.lower() != "jerry":
    portion_quantity = int(input("How many portions of soup? "))
    total = portion_price * portion_quantity

    print(f"The total cost is {total:,.2f}")

print("Next please!")

number = int(input("Please a number: "))
quotient = number // 10
message = ""

if number >= 0:
    if quotient >= 10:
        message = "This number is smaller than 1000"
    elif quotient >= 1:
        message = """
This number is smaller than 1000
This number is smaller than 100"""
    elif quotient == 0:
        message = """
This number is smaller than 1000
This number is smaller than 100
This number is smaller than 10"""
    print(message)
    print("Thank you!")
else:
    print("Negative number not allowed!")


"""
Calculator
"""

number1 = float(input("Number 1: "))
number2 = float(input("Number 2: "))
operation = input("Operation (add, multiply, subtract): ").lower()

if operation == "add":
    calculus = number1 + number2
    print(f"{number1} + {number2} = {calculus}")
elif operation == "multiply":
    calculus = number1 * number2
    print(f"{number1} x {number2} = {calculus}")
elif operation == "subtract":
    calculus = number1 - number2
    print(f"{number1} - {number2} = {calculus}")

"""
Temperature
"""

temperature_in_fahrenheit = int(input("Please type in the temperature (°F): "))

if temperature_in_fahrenheit <= 0:
    print("Brr! It's cold in here!")
else:
    temperature_in_degree = (temperature_in_fahrenheit - 32) * 9/5
    print(f"{temperature_in_fahrenheit}°F = {temperature_in_degree:,.2f}°C")

"""
Daily Wages
"""
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
weekday = input("Day of the week: ").strip()

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

text = f"""
Hourly wage: {hourly_wage}
Hours worked: {hours_worked}
Day of the week: {weekday}
"""

if weekday not in weekdays:
    print("Closed company!")
else:
    daily_wage = hourly_wage * hours_worked

    if weekday == "Sunday":
        daily_wage *= 2

    print(text)
    print(f"Daily wages: {daily_wage} euros")

"""
Solving a quadratic equation
aX2 + bX + c = 0
"""

from math import pow, sqrt

a = float(input("Value of a: "))
b = float(input("Value of b: "))
c = float(input("Value of c: "))

delta = pow(b, 2) - 4 * a * c

x1, x2 = None, None

if delta < 0:
    print("No solution of equation")
elif delta == 0:
    x1 = -b / (2 * a)
    print(f"x1 = {x1}")
else:
    x1 = (-b - sqrt(delta)) / (2 * a)
    x2 = (-b + sqrt(delta)) / (2 * a)
    print(f"x1 = {x1}, x2 = {x2}")




