
import csv

year1 = int(input("Enter a starting year: ").strip())
year2 = int(input("Enter a end year: ").strip())

reader = list(csv.reader(open('P114_Books.csv')))
tmp = []

for row in reader:
    tmp.append(row)

x = 0

for row in tmp:
    if int(tmp[x][2]) >= year1 and int(tmp[x][2]) <= year2:
        print(tmp[x])
    x = x + 1