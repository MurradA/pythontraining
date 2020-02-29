import random

file = open("P105_Numbers.txt", "w")
for i in range(1,6):
    file.write(str(random.randint(1, 50))+"\n")

file.close()