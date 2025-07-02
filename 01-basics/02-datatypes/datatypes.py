"""
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

# Getting Datatypes

name: str = "Bernard Konan"  # str type
print(f"The type of '{name}' is '{type(name).__name__}'")

product_price: float = 1000.567
product_quantity: int = 500
print(f"""
The type of '{product_price}' is '{type(product_price).__name__}'. And
The type of {product_quantity} is '{type(product_quantity).__name__}.'
""")

"""
Sequence: List, Tuple, Range
"""
# List
names: list[str] = ['Luigi', 'Jane', 'Mario']

if isinstance(names, list):
    print(f"Type of names: '{type(names).__name__}'")
    for index, name in enumerate(names):
        print(f"{index} => {name}")

# Tuple
persons: list[tuple[str, int]] = [('Mario', 28,), ('Luigi', 15,), ('John Doe', 47,)]

for person in persons:
    if isinstance(person, tuple):
        name, age = person
        print(f"name = {name}, age = {age} year{'s' if age > 1 else ''} old")
    else:
        print("You're not a valid person.")

# Range
numbers = range(100)

print(type(numbers))

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print(number)

# Mapping

user: dict[str, str | int] = {"id": 1,
                              "name": "Leanne Graham",
                              "username": "Bret",
                              "email": "Sincere@april.biz",
                              "address": {
                                  "street": "Kulas Light",
                                  "suite": "Apt. 556",
                                  "city": "Gwenborough",
                                  "zipcode": "92998-3874",
                                  "geo": {
                                      "lat": "-37.3159",
                                      "lng": "81.1496"
                                  }
                              },
                              "phone": "1-770-736-8031 x56442",
                              "website": "hildegard.org",
                              "company": {
                                  "name": "Romaguera-Crona",
                                  "catchPhrase": "Multi-layered client-server neural-net",
                                  "bs": "harness real-time e-markets"
                              }
                              }


# print properties and values recursively

def display_key_value(data: dict[str, str | int], indent: int = 0):
    for key, value in data.items():
        prefix = "  " * indent

        if isinstance(value, dict):
            print(f"{prefix}[{key}]:")
            return display_key_value(value, indent=indent + 1)
        else:
            print(f"{prefix}{key} => {value}")


display_key_value(user)

# Set Types
fruits: set[str] = {"Banana", "Cherry", "Pineapple", "Apple"}

print("Set type: ", type(fruits), fruits)

for fruit in fruits:
    print(fruit)
