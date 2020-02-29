compnum = 50
attempts = 1

num = int(input("Guess a number: ").strip())
while num != compnum:
    if num > compnum:
        print("Too high")
    else:
        print("Too low")

    attempts += 1
    num = int(input("Guess another number: ").strip())

print("Well done, you took {0} attempts".format(attempts))
