import random

number = random.randint(1, 100)
guess = 0
ask = -1  # intially

while (ask != number):
    try:
        ask = int(input("Guess the number (between 1 and 100): "))
        guess += 1
        if ask < number:
            print("Too low! Try again.")
        elif ask > number:
            print("Too high! Try again.")
        else:
            print(
                f"Congratulations! You guessed the number in {guess} attempts")
    except Exception as e:
        print(e)
