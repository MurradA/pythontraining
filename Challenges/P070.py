countries = ("UK", "USA", "FRANCE", "SPAIN", "MEXICO")
print(countries)

print("")

choose = input("Choose a country from the five listed above: ").strip()
print(choose.upper(), "has index number", countries.index((choose.upper())))

print("")

num = int(input("Enter a number (0 - 4) to find the country's position in the Tuple: ").strip())
print("In index", num, "is the country:", countries[num])

