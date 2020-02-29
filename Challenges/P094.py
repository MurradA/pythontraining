from array import *

nums = array('i',[23,45,64,32,12])

print(nums)


tryagain = True

while tryagain == True:

    select = int(input("Select a number from the array: ").strip())

    if select in nums:
        print("\nThe number you selected is in index:", nums.index(select))
        tryagain = False
    else:
        print("Try again!")
        continue