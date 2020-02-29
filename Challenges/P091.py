from array import *

num_array = array('i',[1,5,9,4,9])

print(num_array)

num1 = int(input("Enter a number from the array:").strip())

if num_array.count(num1) == 1:
    print(num1, "is in the list once.")
else:
    print(num1, "is in the list", num_array.count(num1), "times.")



