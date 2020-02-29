from array import *

nums = array('d',[12.12,22.22,32.32,42.42,52.52])
div = []
print(nums)
tryagain = True

while tryagain == True:
    num1 = int(input("\nEnter a whole number between 2 and 5: ").strip())

    if num1 < 2 or num1 > 5:
        print("\nOutside of range, try again!")
    else:
        for val in nums:
            sum = val / num1
            div.append(sum)
            tryagain = False

for i in div:
    print(i)


# Book Solution:

# nums = array('f',[12.12,22.22,32.32,42.42,52.52])
# tryagain = True

# while tryagain == True:
#     num1 = int(input("\nEnter a whole number between 2 and 5: ").strip())
#     if num1 < 2 or num >5:
#         print("Inccorect, try again.")
#     else:
#         tryagain = False

# for i in range(0,5):
#     ans = nums[i]/num1
#     print(round(ans,2))





