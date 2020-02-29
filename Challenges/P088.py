from array import *

num_array = array('i',[])
num = int(input("Enter a number: ").strip())
num_array.append(num)
for i in range(0, 4):
    num = int(input("Enter another number: ").strip())
    num_array.append(num)

num_array = sorted(num_array)
num_array.reverse()

print(num_array)


