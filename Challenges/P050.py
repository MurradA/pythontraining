num = int(input("Guess a number between 10 and 20: ").strip())

while num != (10 <= num <= 20):
    if num < 10:
        print("Too Low")
        num = int(input("Guess another number: ").strip())
    elif num > 20:
        print("Too High")
        num = int(input("Guess another number: ").strip())
    else:
        break

print("Thank you!")
