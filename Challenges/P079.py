nums = []
for i in range(0, 3):
    num = int(input("Enter a number: ").strip())
    nums.append(num)

print(nums)

confirm = input("\n The last number you entered was: {0} \n\nDo you wish to remove that number in the list? (y/n): ".format(nums[(len(nums)-1)])).strip().lower()

if confirm == "y":
    nums.pop((len(nums)-1))

print("\n", nums)

