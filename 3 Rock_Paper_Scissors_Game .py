import random

emoji = {
    1: "🪨",
    0: "📃",
    -1: "✂️"
}
userChoice = {
    "r": 1,
    "p": 0,
    "s": -1
}


def game():
    round_numb = 1
    computer_wins = 0
    user_wins = 0

    while user_wins < 2 and computer_wins < 2:
        print(f"\nRound {round_numb}")

        user = input("Rock, Paper or Scissors? (r/p/s): ").lower()
        if user not in userChoice:
            print("Invalid")
            continue

        # Get user choice value
        mainUser = userChoice[user]  # user = "r" → userChoice["r"] returns 1
        # Computer makes a random choice
        computer = random.choice([1, 0, -1])
        print(f"You chose {emoji[mainUser]}\nComputer chose {emoji[computer]}")

        if (mainUser == computer):
            print("Tie! Try again")
        else:
            if ((mainUser == 1 and computer == 0) or (mainUser == 0 and computer == -1) or (mainUser == -1 and computer == 1)):
                print("You lose")
                computer_wins += 1
            elif ((mainUser == 1 and computer == -1) or (mainUser == 0 and computer == 1) or (mainUser == -1 and computer == 0)):
                print("You win")
                user_wins += 1
        round_numb += 1

    # final result
    if user_wins == 2:
        print("You won the best of 3")
    else:
        print("Computer won the best of 3")

        # continue
        ask = input("Continue? (y/n): ")
        if (ask == "y"):
            game()
        else:
            print("Thanks for playing")


game()
