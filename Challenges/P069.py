countries = ("UK", "USA", "FRANCE", "SPAIN", "MEXICO")
print(countries)
choose = input("Choose a country from the five listed above: ").strip()
print(choose.upper(), "has index number", countries.index((choose.upper())))
