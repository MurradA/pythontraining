import random

num = random.randint(1, 10)
guess = int(input("Guess the number I'm thinkning of. Hint: It's between 1 and 10:").strip())

while guess != num:
    guess = int(input("Wrong - Try again!\nGuess another number between 1 and 10:").strip())

print("Congratulations you got it right!")
