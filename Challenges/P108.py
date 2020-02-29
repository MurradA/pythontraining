file = open("P106_Names.txt", "a")

name = input("Enter a name: ").strip()

file.write(name)

file.close()