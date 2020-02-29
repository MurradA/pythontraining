nums = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

for i in nums:
    print(i)

row = int(input("Select a row (1 - 4): ").strip())
col = int(input("Select a column (1 - 3): ").strip())

print(nums[(row - 1)][(col - 1)])