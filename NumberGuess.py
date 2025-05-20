import random
RandomNumb = random.randrange(1, 200)
UserInput = int(input("Enter the number: "))

if UserInput > RandomNumb:
    print(RandomNumb)
    print("The number is too high")
elif UserInput < RandomNumb:
    print(RandomNumb)
    print("The numb is too low")
else:
    print(RandomNumb)
    print("Congratulations! You matched the number")
