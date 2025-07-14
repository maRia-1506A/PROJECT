name = input("Type your name: ")
ans = input(f"Welcome {name}! Do you want to play? [y/n]: ").lower()

while ans == 'y':
    print("Welcome To The Adventure Game!")
    ask1 = input(
        "You're standing at the edge of a dark forest.\nDo you want to go into the forest or walk along the river? ")

    if ask1 == 'forest':
        ask2 = input("\nYou walk into the forest. Its quite dark and when you start walking, its getting darker and darker.\nOnce you see a cave and a tall tree nearby. Do you want to enter the cave or climb the tree? ")

        if ask2 == 'tree':
            ask3 = input("\nYou climb the tree and find a nest of golden eggs. You take one and carefully climb down.\nSuddenly, a dragon appears looking for its egg! Do you run or hide? ")

            if ask3 == 'hide':
                print("\nYou hide under some bushes. The dragon doesn't see you and flies away!\nYou survived and keppt the golden egg!🎊🎉")
                print("Congratulations!! YOU WIN🏆🏆")

            elif ask3 == 'run':
                print(
                    "\nThe dragon is faster than you, so it catches you. You lose the game!")

            else:
                print("Not a valid option. You lose the game!")

        elif ask2 == 'cave':
            print(
                "\nYou've just wake up a sleepy bear! So it just ate you & you lose the game!:)")

        else:
            print("Not a valid option. You lose the game")

    elif ask1 == 'river':
        print("\nThere is crocodile in the river🐊🐊. You die ＞﹏＜")
    else:
        print("Not a valid option. You lose the game")

    ask = input("Do you want to play again?[y/n]: ")
