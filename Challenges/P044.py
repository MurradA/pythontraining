total = int(input("How many people do you want to invite to your party?: ").strip())
if total < 10:
    for i in range (0, total):
        name = input("Send invite to: ").strip()
        print("{0} has been invited.".format(name))
else:
    print("Too many people!")