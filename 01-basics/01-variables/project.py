"""
This Python project is a simple command-line currency converter that allows users to convert amounts from West
African CFA franc (XOF) to either:
    🔴 US Dollar (USD)
    🔴 Euro (EUR)
"""
from enum import Enum


class Currency(Enum):
    """
    Enumeration for supported currencies.
    """
    EURO: str = "EURO"
    DOLLAR: str = "DOLLAR"


def converter_currency(amount: float, currency: Currency) -> float:
    """
        Converts a given amount in Fcfa to the specified currency (EURO or DOLLAR).

        Args:
            amount (float): The amount in Fcfa to convert.
            currency (Currency): The target currency as a Currency enum.

        Returns:
            float: The converted amount, rounded to two decimal places.

        Raises:
            NotImplementedError: If the specified currency is not supported.
    """
    match currency:
        case Currency.EURO:
            return round(amount / 655, 2)
        case Currency.DOLLAR:
            return round(amount / 600, 2)
        case _:
            raise NotImplementedError(f"Conversion to {currency} is not implemented.")


def display_menu() -> None:
    """
    Displays the conversion menu to the user.
    """
    print("\n🔁 Currency Converter: Fcfa to USD / EURO 🔁")
    print("1 - Convert Fcfa to USD")
    print("2 - Convert Fcfa to EURO")
    print("0 - Exit")


def main() -> None:
    """
    Main program loop to handle user interaction.
    """

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("GoodBye")
            break

        if choice not in ("1","2"):
            print("❌ Invalid choice. Please try again.")
            continue

        try:
            amount = float(input("Enter the amount in Fcfa: "))

            if amount < 0:
                raise ValueError("Amount must be positive.")

            currency: Currency = Currency.DOLLAR if choice == "1" else Currency.EURO
            converted = converter_currency(amount, currency)

            symbol = "$" if currency == Currency.DOLLAR else "€"

            if currency == Currency.DOLLAR:
                print(f"✅ {amount} Fcfa = {symbol}{converted}")
            elif currency == Currency.EURO:
                print(f"✅ {amount} Fcfa = {converted}{symbol}")
        except ValueError as v_error:
            print(f"❌ Invalid input: {v_error}")
        except Exception as e:
            print(f"⚠️ An error occurred: {e}")


if __name__ == '__main__':
    main()
