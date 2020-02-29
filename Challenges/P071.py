sports = ['Football', 'Tennis']
fav = input("Which sport do you enjoy {0}?: ").strip()
sports.append(fav.capitalize())
sports.sort()
print(sports)
