subject = input("Favourite Subject (Enter in uppercase): ").strip()
tryagain = False
while tryagain == False:
    if subject == subject.upper():
        print("\nThank You!")
        tryagain = True
    else:
        subject = input("\nUSE UPPERCASE - Favourite Subject: ").strip()





