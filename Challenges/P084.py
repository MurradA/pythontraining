postcode = input("Enter your postcode: ").strip()
start = postcode[0:2]
print("{0}{1}".format(start.upper(), postcode[2:]))
