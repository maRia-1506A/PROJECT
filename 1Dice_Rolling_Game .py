# ask: roll the  dice
# if say yes then generate two number and print


import random

diceRoll = 0
while True:
    try:
        ask = input("Roll the dice? (y/n): ").lower()
        if ask == "y":
            roll1 = random.randint(1, 6)
            roll2 = random.randint(1, 6)
            print(f"({roll1},{roll2})")
            diceRoll += 1

        elif ask == "n":
            print("Game over!")
            print(f"You rolled {diceRoll} times!")
            break
        else:
            print("Invalid choice")
    except Exception as e:
        print(f"An error occured! {e}")
        print("Try again!")
