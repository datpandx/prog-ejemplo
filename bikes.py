import csv
with open("bikes2.csv", 'r') as file:
    csvr = csv.reader(file)

    for row in csvr:
        print(row)
