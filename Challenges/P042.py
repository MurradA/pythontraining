total = 0

for i in range(0, 5):
    q = int(input("Enter a number: ").strip())
    n = input("Do you want that number included? (y/n): ").strip()

    if n.lower() == "y":
        total = total + q


print(total)