"""
Number Guessing Game

Good answer corresponds to 1 pts
Wrong answer corresponds to 0
"""
from random import randint

# Print some statements
print("------ Welcome to the Guessing Game -------")
print("I'm thinking of a number between 1 and 10")


# utils
def is_convertible_to_number(value: str) -> bool:
    try:
        converted = float(value)
        return isinstance(converted, float)
    except ValueError:
        return False


# Get User Infos
username: str = input("Enter Your name: ")

# Game
score: int = 0
MAX_ATTEMPT: int = 3
secret_number: int = randint(0, 10)

attempt: int = 1

while True:
    response: str = input("Guess the number (Type Q or q to quit): ").strip()

    if not is_convertible_to_number(response):
        print(f"'{response}' is not a valid number! retry")
        continue

    response_number: int = int(response)

    if response_number == secret_number:
        score += 1
        secret_number = randint(0, 10)
        print("Congratulations 🥳. You won 1 pt")
    elif response_number < secret_number:
        print("Too low!🥲 try again.")
    else:
        print("Too high!😒 Try again.")

    if response.lower() == "q" or attempt % MAX_ATTEMPT == 0:
        confirm_quit = input("✅ Do you want to quit ? (Y/N): ")

        if confirm_quit.lower() in ("y", "yes"):
            print("End of the game ➡️➡️")
            break
        else:
            print("➡️➡️ Game continue ...")
            secret_number = randint(0, 10)

    attempt += 1

score_stats: float = round(score / attempt, 2)

if score > 0:
    print(f" {username}, you won {score} pts after {attempt} attempts.")

    if score_stats > 0.5:
        print("➡️➡️ Good Game Score")
    else:
        print("🔴🔴 Bad Game Score")

else:
    print("❌❌ You didn't win anything.")
