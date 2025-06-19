'''
1 for snake
-1 for water
0 for gun
'''
import random
computer = random.choice([1, -1, 0])  # variable 1
user = input("Enter your choice(s/w/g): ")
userChoice = {
    "s": 1,
    "w": -1,
    "g": 0
}
mainUser = userChoice[user]  # variable 2
reverseUserCoice = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}  # to print the choices

print(
    f"You chose {reverseUserCoice[mainUser]}\nComputer chose {reverseUserCoice[computer]}")

if (computer == mainUser):
    print("Game Draw!")
else:
    if ((computer-mainUser) == 1 or (computer-mainUser) == -2):
        print("You Win!")
    else:
        print("You Lose!")
'''
    if (computer == 1 and mainUser == -1): computer-mainUser = 2
        print("You Lose!")
    elif (computer == 1 and mainUser == 0): computer-mainUser = 1
        print("You Win!")
    elif (computer == -1 and mainUser == 1): computer-mainUser = -2
        print("You Win!")
    elif (computer == -1 and mainUser == 0): computer-mainUser = -1
        print("You Lose!")
    elif (computer == 0 and mainUser == -1): computer-mainUser = 1
        print("You Win!")
    elif (computer == 0 and mainUser == 1): computer-mainUser = -1
        print("You Lose!")
    else:
        print("Something went wrong!")
'''
