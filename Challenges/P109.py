import sys

tryagain = True

while tryagain == True:

    print("Select from the following options:")
    print("1) Create a new file")
    print("2) Display the file")
    print("3) Add a item to the file\n")
    select = int(input("Enter 1 , 2, 3 or 0 to end: ").strip())

    if select == 1:
        subject = input("Enter a subject name: ").strip()
        file = open("P109_Subjects.txt", "w")
        file.write(subject+"\n")
        file.close()

    elif select == 2:
        file = open("P109_Subjects.txt", "r")
        print(file.read())
    elif select == 3:
        subject = input("Enter a subject name: ").strip()
        file = open("P109_Subjects.txt", "a")
        file.write(subject + "\n")
        file.close()
    elif select == 0:
        tryagain = False
    else:
        print("Invalid entry")

file.close()
print("System Terminated")
sys.exit()
