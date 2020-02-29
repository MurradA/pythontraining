num1 = int(input("Enter a number:").strip())
num2 = int(input("Enter a number:").strip())
sum = num1 + num2
add = "y"

while add == "y":
    add = input("Do you want to add another number (y/n): ").strip()
    if add.lower() == "y":
        num3 = int(input("Enter a number:").strip())
        sum = sum + num3
    else:
        break

print("The total is ", sum)