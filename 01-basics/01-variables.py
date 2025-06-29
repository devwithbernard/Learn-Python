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
