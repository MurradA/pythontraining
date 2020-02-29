file = open("P106_Names.txt", "r")
print(file.read())
file.close()

file = open("P106_Names.txt", "r")
name = input("\nEnter a name from the list: ").strip().capitalize()
name = name+"\n"
for line in file:
    if line != name:
        file = open("P110_Names.txt", "a")
        newrecord = line
        file.write(newrecord)
        file.close()
file.close()

file = open("P110_Names.txt", "r")
print(file.read())
file.close()







