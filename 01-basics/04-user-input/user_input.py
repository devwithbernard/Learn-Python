"""
Accept user input
"""

name: str = input("Enter your name: ")
age: str = input("Enter your age: ")

print(f"{name} have {age} years old.")

# Exercise 1: Rectangle Area Calculus

length: float = float(input("Enter the length of rectangle: "))
width: float = float(input("Enter the width of rectangle: "))

area: float = length * width

print(f"The area of rectangle with length = {length} cm and width = {width} cm is: {area} cm²")

# Exercise 2: Shopping Cart Program

item: str = input("What item would you like to buy?: ")
price: float = float(input("What is the price?: "))
quantity: int = int(input("How many do you like ?: "))

total: float = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")
