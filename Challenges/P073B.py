foods = {}

for i in range (1, 5):
    fav = input("Enter favourite food item {0}: ".format(i)).strip().capitalize()
    foods[i] = fav

print("")

print(foods)

remove = input("Which food item do you wish to remove from the list? : ").strip().capitalize()

for i in range(1, 5):
    if remove == foods[i]:
        foods.pop(i)

foods = sorted(foods.values())
print(foods)


