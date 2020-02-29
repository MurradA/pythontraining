import csv

file = open("P115_Books.csv" , "r")
x = 0

for row in file:
    display = "Row: "+ str(x) + " - " + row
    print(display)
    x = x + 1
