import datetime
import csv

def inloggers():
    nieuwCSV = open("inloggers.csv" , 'w', newline="")      #filename = inloggers.csv  -   eindigt met enter, "nieuwCSV" alleen binnen Python
    schrijver = csv.writer(nieuwCSV, delimiter=";")             #csv.writer = python operator.
    schrijver.writerow(("Tijdstip", "naam", "voorletter", "Geboortedatum", "Mailadres")) #Rij met titels
    vandaag = datetime.datetime.today()
    tijd = vandaag.strftime("%a %d %b %Y %I:%M:%S %p")

    while True:
        naam = input("Wat is je achternaam? ")
        if naam == "":
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")

        schrijver.writerow((tijd, naam, voorl, gbdatum, email))


print(inloggers())