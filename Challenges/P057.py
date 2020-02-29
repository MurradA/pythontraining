import random

num = random.randint(1, 10)
print(num)
guess = int(input("Guess the number I'm thinkning of. Hint: It's between 1 and 10:").strip())

while guess != num:
    if guess > num:
        print("Too high")
    else:
        print("Too low")

    guess = int(input("Wrong - Try again!\nGuess another number between 1 and 10:").strip())

print("Congratulations you got it right!")
