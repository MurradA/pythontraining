import csv
count = 0
file = open('P113_Books.csv', 'r')
print(file.read())
file.close()

num = int(input("\nHow many records would you liked to add to the file?: ").strip())

for i in range(0, num):
    Book = input("\nEnter a book name: ").strip().capitalize()
    Author = input("Enter the author: ").strip().capitalize()
    Year = int(input("Enter the year the book was published: ").strip())
    newRecord = "{0},{1},{2}\n".format(Book, Author, Year)
    file = open('P113_Books.csv', 'a')
    file.write(newRecord)
    file.close()

file = open('P113_Books.csv', 'r')
search = input("Enter a name of an author: ").strip().capitalize()
reader = csv.reader(file)

for row in file:
    if search in str(row):
        count += 1

if count >= 1:
    print("There are {0} books by {1}".format(count, search))
else:
    print("There are no books by that author")