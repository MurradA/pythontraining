choice = input("Choose from the following options\n1) Square\n2) Triangle\n\nChoose 1 or 2:").strip()
if choice == "1":
    l = float(input("Enter the length of one of the sides of the square:").strip())
    area = l**2
    print("The area of the square is: "+str(area))
elif choice =="2":
    b = float(input("Enter the length of the triangle base:").strip())
    h = float(input("Enter the height of the triangle:").strip())
    area = (b*h)/2
    print("The area of the triangle is: " + str(area))
else:
    print("Choice not recognised!")
