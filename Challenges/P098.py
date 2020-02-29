nums = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in nums:
    print(i)

row = int(input("\nSelect a row to display (1 - 4): ").strip())

print(nums[row-1])

num = int(input("\nEnter a number to add to that row: ").strip())

nums[row-1].append(num)

print(nums[row-1])
