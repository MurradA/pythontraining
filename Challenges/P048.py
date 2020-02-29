count = 0

name = input("Enter a friends name: ").strip()
print(name, " has been invited to the party.")
count += 1

inv = "y"

while inv.lower() == "y":
    add = input("Do you want to invite someone else to the party? (y/n): ").strip()
    if add.lower() == "y":
        name = input("Enter a friends name: ").strip()
        print(name, " has been invited to the party.")
        count += 1
    else: break

print(count, " people are invited to the party.")



