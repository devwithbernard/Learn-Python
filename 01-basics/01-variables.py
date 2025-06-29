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
