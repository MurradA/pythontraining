tv_shows =['The Vampire Diaries', 'The Originals', 'Legacies', 'Supernatural']

for i in tv_shows:
    print(i)

new_show = input("\nEnter the name of another show you watch: ").strip().capitalize()
pos = int(input("\nEnter where in the list do you wish to position {0}. Choose a position between 1 - 5: ".format(new_show)).strip())

tv_shows.insert(pos-1, new_show)

print("")

for i in tv_shows:
    print(i)

