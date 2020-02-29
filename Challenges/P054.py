import random

choice = input("Choose h for heads, t for tails or any other key to end:").strip().lower()

flip = random.choice(["h", "t"])

while choice != "x":

    if flip == choice:

        if flip == "h":
            print("Heads it is - You win!")
        else:
            print("Tails it is - You win!")

    elif flip != choice:

        if flip == "h":
            print("Bad luck - it was heads")
        else:
            print("Bad luck - it was tails")
    else:
        break

    choice = input("Choose h for heads, t for tails or any other key to end: ").strip().lower()

    flip = random.choice(["h", "t"])

print("Thanks for playing.")