"""
Casting in python:

int -> str
int -> float

float -> str
float -> int

str -> int if 'str' in a valid number after conversion
str -> float if 'str' in a valid number after conversion
"""

fruit: str = "Mango"
fruit_price: float = 3.75
fruit_quantity: int = 10

total_price: float = fruit_price * fruit_quantity

# Print variables and their types
# print(fruit, type(fruit))
# print(fruit_price, type(fruit_price))
# print(fruit_quantity, type(fruit_quantity))

# Type casting
fruit_price_str = str(fruit_price)
print(f"{fruit} cost ${fruit_price_str}")

fruit_quantity_float = float(fruit_quantity)
print(f"She bought {fruit_quantity} {fruit.lower()}. It cost ${total_price}")