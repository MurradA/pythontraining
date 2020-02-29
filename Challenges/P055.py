import random
ran = random.randint(1, 5)
num = int(input("Guess a number between 1 and 5:").strip())

if num == ran:
    print("Well done")
elif num > ran:
    print("Too high")
    num = int(input("Try again Guess a number between 1 and 5:").strip())
    if num == ran:
        print("Correct")
    else:
        print("You Lose!")
elif num < ran:
    print("Too low")
    num = int(input("Try again Guess a number between 1 and 5:").strip())
    if num == ran:
        print("Correct")
    else:
        print("You Lose!")

