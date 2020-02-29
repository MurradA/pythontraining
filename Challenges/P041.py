name = input("Enter your name: ").strip()
num = int(input("Enter a number: ").strip())

if num < 10:
    for i in range(0, num):
        print(name)
else:
    for i in range(0,3):
        print("Too High")
