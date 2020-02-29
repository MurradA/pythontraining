data_set = {}

for i in range(0,4):
    name = input("Enter your name: ").strip().capitalize()
    age = int(input("Enter your age: ").strip())
    shoesize = float(input("Enter your shoe size: ").strip())
    data_set[name] = {'Age':age,
                      'Shoe Size:':shoesize}
for names in data_set:
    print((names), data_set[names]['Age'])