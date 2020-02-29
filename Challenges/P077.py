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

            index = names.index(i)

            print(i, "-", index)

        remove = input("\nDo you want to UN-INVITE anyone on the list? (y/n): ").strip().lower()
        if remove == "n":

            print("\nThe following people are invited to your party: ")

            for x in names:

                print(x)

            break

        elif remove == "y":
                uninvite = int(input("\nEnter the person's corresponding number to remove them: ").strip().lower())
                for i in names:
                    if uninvite == names.index(i):
                        names.pop(uninvite)
                continue
        else:
            print("\Invalid Entry")

    else:
        print("\nInvalid entry")

print("\nHave an awesome party! WooHooo!")
