match = 0
success = 0
tryagain = True

while tryagain == True:
    password = input("Enter Password: ").strip()
    c_password = input("Confirm Password: ").strip()

    if password == c_password:
        success = success + 1
        if success > 0:
            print("Thank you!")
            tryagain = False
        break
    else:
        for i in password:
            for x in c_password:
                if i == x.upper() or i == x.lower():
                    match = match + 1
                else:
                    match = 0

    if match > 0:
        print("The need to be the same case!")
    else:
        print("Incorrect")

print("Access Granted!")

