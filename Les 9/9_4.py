import csv

with open("tabel.csv") as tabel:
    lezer = csv.DictReader(tabel, delimiter=";")



#naam en prijs van duurste product
