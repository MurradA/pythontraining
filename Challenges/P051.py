bottles = 10

while bottles > 0:
    print("There are {0} green bottles hanging on the wall,\n{0} green bottles hanging on the wall,\nand if 1 green bottle should accidentally fall.".format(bottles))
    guess = int(input("How many green bottles will be hanging on the wall? : ").strip())
    bottles = bottles - 1

    if bottles == guess:
        print("There will be ", bottles, " green bottles hanging on the wall.")

    else:
        while guess != bottles:
            guess = int(input("Wrong - Try again! How many green bottles will be hanging on the wall? : ").strip())

print("There are no more green bottles hanging on the wall")
