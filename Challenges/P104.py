data_set = {}

for i in range(0,4):
    name = input("Enter your name: ").strip().capitalize()
    age = int(input("Enter your age: ").strip())
    shoesize = float(input("Enter your shoe size: ").strip())
    data_set[name] = {'Age':age,
                      'Shoe Size':shoesize}

for i in data_set:
    print(i, data_set[i])

del_name = input("\nEnter your name: ").strip().capitalize()

if del_name in data_set:
    del data_set[del_name]

for i in data_set:
    print(i, data_set[i]['Age'], data_set[i]['Shoe Size'])