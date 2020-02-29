num_list = [159, 874, 563, 200]

for i in range(0, 4):
    print(num_list[i])

num = int(input("Enter a 3 digit number: ").strip())

if num in num_list:
    print(num_list.index(num))
else:
    print("{0} isn't in the list.".format(num))

