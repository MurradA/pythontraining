data_set = {}

for i in range(0,4):
    name = input("Enter your name: ").strip().capitalize()
    age = int(input("Enter your age: ").strip())
    shoesize = float(input("Enter your shoe size: ").strip())
    data_set[name] = {'Age':age,
                      'Shoe Size:':shoesize}

print(data_set)

tryagain = True

while tryagain == True:
    name = input("Enter your name: ").strip().capitalize()

    if name in data_set:
        print(data_set[name])
        tryagain = False
    else:
        print("Name not in dataset.")


