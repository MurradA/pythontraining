direction = input("Count 'up' or 'down': ").strip().lower()

if direction == "up":
    top = int(input("Enter the top number: ").strip())
    for i in range(1, top+1, 1):
        print(i)
elif direction == "down":
    num = int(input("Enter a number less than 20: ").strip())
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don't understand your selection.")