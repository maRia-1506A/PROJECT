import random
dice = True

while dice:
    print(random.randint(1, 6))
    ask = input("Do you want to roll again? [y/n]: ")

    if ask == "y":
        continue
    else:
        print("Game Over!")
        break
