nums = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in nums:
    print(i)

row = int(input("\nSelect a row (1 - 4): ").strip())
col = int(input("Select a column from that row (1 - 3): ").strip())

print('The value you have chosen is:', nums[row-1][col-1])

confirm = input("\nDo you wish to change that number (y/n) ").strip().lower()

if confirm == 'y':
    num = int(input("\nEnter a new number: ").strip())
    nums[row-1][col-1] = num
    print('Row has been changed to', nums[row - 1])


print("")

for i in nums:
    print(i)

print("\nThe End!")