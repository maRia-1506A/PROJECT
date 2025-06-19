# import random
# RandomNumb = random.randrange(1, 200)
# UserInput = int(input("Enter the number: "))

# if UserInput > RandomNumb:
#     print(RandomNumb)
#     print("The number is too high")
# elif UserInput < RandomNumb:
#     print(RandomNumb)
#     print("The numb is too low")
# else:
#     print(RandomNumb)
#     print("Congratulations! You matched the number")


import random
randomNumb = random.randint(1, 100)
guess = 0
a = -1  # Initialize with -1 before using it in while loop

while (a != randomNumb):
    guess += 1
    a = int(input("Guess anumber: "))
    if (a > randomNumb):
        print("Lower number please!")
    else:
        print("Higher Number please!")

print(f"You have guessed the correct number {randomNumb} in {guess} guesses")
