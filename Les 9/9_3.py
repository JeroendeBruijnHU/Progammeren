import csv

with open("scorelijst.csv", 'r') as CSVFILE:
    lezer = csv.reader(CSVFILE, delimiter=";")

    for row in lezer: #row = dict
        #print("Score: {}".format(row[2]))
        print("De hoogste score is", ("{}".format(row[2])), "op", ("{}".format(row[1]) ), "behaald door", ("{}".format(row[0])))