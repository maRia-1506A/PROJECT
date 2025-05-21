answer = input("Do you want to play this game? [Yes/No]: ")

if answer == "yes":
    print("Welcome to the game!")
    answer = input("Do you want to go to jungle or cave? [jungle/cave]: ")

    if answer == "jungle":
        print("You see the hungry tiger. The tiger will eay you! You're done. END GAME")
    elif answer == "cave":
        print("You see a bear sleeping in front of you")
        answer = input("Do you want run or fight with the bear? [fight/run]: ")

        if answer == "fight":
            print("The bear is too strong. You lost the game!")
        else:
            print("WOAH! You survived the game.")
            print("Thank You!")
else:
    print("The game is closed")
