name = input("Enter your name: ").strip().capitalize()
vowels = ["a","e","i","o","u","A","E","I","O","U"]
count = 0
for i in name:
    for x in vowels:
        if i == x:
            count += 1

print(name, "has", count, "vowels in it.")

