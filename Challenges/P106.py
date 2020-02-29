file = open("P106_Names.txt", "w")

for i in range(0,5):
    name = input("Enter a name: ").strip()
    file.write(name+"\n")

file.close()