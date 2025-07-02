"""
Display data type
"""
from collections.abc import Iterable

values = [3.141592, 15, None, "Hello world", dict(name="Konan Bernard", age=28), ['Orange', "Pineapple"]]


def display_data_type(data: Iterable, indent: int = 0):
    for item in data:
        prefix = "  " * indent
        if isinstance(item, Iterable) and not isinstance(item, str) and not dict:
            display_data_type(item, indent + 1)
        elif isinstance(item, dict):
            display_data_type(item.values(), indent + 1)
        else:
            print(f"{prefix}{item} => '{type(item).__name__}'")


display_data_type(values)