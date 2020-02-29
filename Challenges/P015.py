colour = input("Enter your favourite colour:".strip())
red = "red"

if colour == red or colour == red.upper() or colour == red.title():
    print("I like red too")
else:
    print("I don't like {0}, I prefer red.".format(colour))

