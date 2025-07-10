# ask: roll the  dice
# if say yes then generate two number and print


import random

while True:
    ask = input("Roll the dice? (y/n): ").lower()
    if ask == "y":
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        print(f"({roll1},{roll2})")
    elif ask == "n":
        print("Game over!")
        break
    else:
        print("Invalid choice")
