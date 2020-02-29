num = int(input("Enter a number between 10 - 20: ".strip()))

if num < 10:
    print("Too Low")
elif 10<= num <=20:
    print("Correct Input")
else:
    print("Too High")