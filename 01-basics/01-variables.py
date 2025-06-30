"""
Title: Python Variables - Introduction

Description:
This script introduces the concept of variables in Python. It covers:
- What a variable is
- How to assign values to variables
- Naming conventions
- Multiple assignments
- Variable types and dynamic typing

Author: [Your Name]
Date: [Date]
"""

# Assign a variable
name: str = "John Doe"
age: int = 28

print(f"Your name is {name}.\nAnd you have {age} year{'s' if age > 1 else ''} old.")

product_name: str = "Renault 200"
product_brand: str = "Renault"
product_price: float = 10_000_000.25
product_available: bool = True

message: str

if product_available:
    message = f"""
    Product (🚗)
        Name: {product_name}
        Price: ${product_price:.2f}
        Brand: {product_brand}
    """
else:
    message = "🔴Product not available."

print(message)


# Multiple assignment
user_name, user_email, user_is_connected, user_session = "Jack Ma", "jackma@gmail.com", True, "Offline"

if user_is_connected:
    user_session = "Online"
    print(f"User with name = '{user_name}' and email = '{user_email}' is connected.")

    if user_session is not None:
        print(f"You can edit your profile page.")
else:
    print(f"User with name = '{user_name}' is not connected.")

# Casting
# List of car products with brand and price
cars: list[dict[str, str | float]] = [
    {"brand": "Toyota", "model": "Corolla", "price": 20000, "currency": "EURO"},
    {"brand": "Honda", "model": "Civic", "price": 22000, "currency": "DOLLAR"},
    {"brand": "Ford", "model": "Focus", "price": 21000, "currency": "EURO"},
    {"brand": "BMW", "model": "3 Series", "price": 35000, "currency": "EURO"},
    {"brand": "Audi", "model": "A4", "price": 37000, "currency": "DOLLAR"},
    {"brand": "Hyundai", "model": "Elantra", "price": 19000, "currency": "EURO"},
    {"brand": "Kia", "model": "Forte", "price": 18500, "currency": "DOLLAR"},
    {"brand": "Mercedes-Benz", "model": "C-Class", "price": 40000, "currency": "DOLLAR"},
    {"brand": "Tesla", "model": "Model 3", "price": 43000, "currency": "DOLLAR"},
    {"brand": "Nissan", "model": "Sentra", "price": 19500, "currency": "EURO"},
]


def convert_euro_to_dollar(product: dict[str, str | float]) -> dict[str, str | float]:
    """
    Converts the price of a product from euros to dollars if its currency is 'EURO'.

    The function assumes the product dictionary contains the keys 'price' and 'currency'.
    If the currency is 'EURO', the price is converted to USD using a fixed exchange rate
    (1 EUR = 1.17 USD). The converted price replaces the original value in the dictionary.

    Args:
        product (dict[str, str | float]): A dictionary representing a product with at least
        'price' (float) and 'currency' (str) keys.

    Returns:
        dict[str, str | float]: The updated product dictionary with the price possibly converted to USD.
    """

    if product['currency'] == "EURO":
        product['price'] *= 1.17  # 1€ = 1.17$
        product['currency'] = "DOLLAR"
        return product
    return product


def total_price(products: list[dict[str, str | float]]) -> float:
    """
    Calculates the total price of a list of products.

    Each product in the list should be a dictionary containing at least a 'price' key
    with an integer or float value.

    Args:
        products (list[dict[str, str | int]]): A list of product dictionaries.
        Each dictionary must contain a 'price' field.

    Returns:
        float: The total price of all products in the list.
    """
    converted_products: list[dict[str, str | float]] = [convert_euro_to_dollar(product) for product in products]
    return float(sum(product['price'] for product in converted_products))


print(f"The total amount of cars is ${total_price(cars)}")
print(cars)
