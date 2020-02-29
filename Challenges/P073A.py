# This was my own little challenge to take input and add to list.

count = 0
fav_food = []
while count != 4:
    for i in range(1, 5):
        if i == 1:
            fav = input("Enter your {0}st favourite food: ".format(i)).strip().capitalize()
            fav_food.append(fav)
            count += 1
        elif i == 2:
            fav = input("Enter your {0}nd favourite food: ".format(i)).strip().capitalize()
            fav_food.append(fav)
            count += 1
        elif i == 3:
            fav = input("Enter your {0}rd favourite food: ".format(i)).strip().capitalize()
            fav_food.append(fav)
            count += 1
        elif i == 4:
            fav = input("Enter your {0}th favourite food: ".format(i)).strip().capitalize()
            fav_food.append(fav)
            count += 1


print(fav_food)
