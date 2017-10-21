import csv

with open("scorelijst.csv", 'r') as CSVFILE:
    lezer = csv.reader(CSVFILE, delimiter=";")

    highscore = 0
    datum = 0
    speler = 0


    for row in lezer:
        if int(row[2]) > highscore:
            highscore = int((row[2]))
            datum = (row[1])
            speler = (row[0])
    print("De hoogste score is",highscore,"behaald op", datum, "door", speler)



