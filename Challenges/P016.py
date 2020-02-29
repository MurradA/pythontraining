isRain = input("Is it raining? (Yes/No):".strip())

if isRain.lower() == "yes":
    isWindy = input("Is it windy? (Yes/No):".strip())
    if isWindy.lower() == "yes":
        print("Is it too windy for an umbrella!".strip())
    else:
        print("Take an umbrella!")
else:
    print("Enjoy your day!")