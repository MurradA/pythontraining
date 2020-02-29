import csv
Book = input("Enter a book name: ").strip()
Author = input("Enter the author: ").strip()
Year = int(input("Enter the year the book was published: ").strip())
newRecord = "{0},{1},{2}\n".format(Book, Author, Year)
file = open('P112_Books.csv','a')
file.write(newRecord)
file.close()


