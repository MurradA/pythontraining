word = input("Enter a random word: ").strip().capitalize()

for i in range((len(word) - 1), -1, -1):
    print(word[i])
