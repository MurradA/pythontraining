from array import *

num = array('i',[])

while len(num) < 5:
    add = int(input("Enter a number to add to the array between 10 and 20:").strip())

    if add >= 10 and add <= 20:
            num.append(add)
    else:
        print("Outside the range.")

print("Thank you!")
for i in num:
    print(i)

