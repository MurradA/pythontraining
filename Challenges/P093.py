from array import *

num = array('i',[])

for i in range(0,5):
    num1 = int(input("Enter a number: ").strip())
    num.append(num1)

num = sorted(num)

print(num)

num1 = int(input("Select a number from the array above to remove: ").strip())

if num1 in num:
    num.remove(num1)
    num2 = array('i',[])
    num2.append(num1)
    print(num)
    print(num2)
else:
    print("Not in array")






