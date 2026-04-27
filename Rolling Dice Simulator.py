import random

while True:
    roll = input("Roll dice? (y/n): ")

    if roll == "y":
        print("🎲", random.randint(1, 6))
    else:
        break