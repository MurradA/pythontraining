names = []
for i in range(0, 3):
    add = input("Enter a name to invite: ").strip().capitalize()
    names.append(add)

add1 = "y"

while add1:

    addmore = input("\nDo you want to invite another person? (y/n): ").strip().lower()

    if addmore == "y":
        add = input("Enter a name to invite: ").strip().capitalize()
        names.append(add)
    elif addmore == "n":

        print("\nThe following people are invited to your party: ")
        for i in names:
            print(i)
        break
    else:
        print("\nInvalid entry")



print("\nHave an awesome party! WooHooo!")