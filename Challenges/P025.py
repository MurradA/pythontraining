fname = input("Enter your first name: ".strip())
if len(fname) < 5:
    lname = input("Enter your last name: ".strip())
    print(fname.upper(),lname.upper())
else:
    print(fname.lower())
