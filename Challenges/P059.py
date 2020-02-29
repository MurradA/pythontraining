import random

colour = ["Red", "Green", "Blue", "Pink", "Purple"]
colour_random = random.choice(["Red", "Green", "Blue", "Pink", "Purple"])

tryagain = True

while tryagain == True:
    guess = input("Guess which colour I'm thinking of {0} :".format(', '.join(colour)).strip())

    if guess.capitalize() == colour_random:
        print("Well Done - You guessed the right colour!")
        tryagain = False
    else:
        if colour_random == "Red":
            print("Roses are red.")
        elif colour_random == "Green":
            print("The grass is greener on the other-side.")
        elif colour_random == "Blue":
            print("Violets are blue.")
        elif colour_random == "Pink":
            print("Pretty in pink.")
        elif colour_random == "Purple":
            print("As purple as a plum.")
