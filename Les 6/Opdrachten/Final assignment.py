#functie 2
def nieuwe_kluis():
    kluisnummers  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    infile = open("kluizen.txt")
    regels = infile.readlines()
    infile.close()

    for regel in regels:
        #mogelijke waarde kan zijn 11:6754
        kluisinfo = regel.split(";")
        # wordt dan 11, 6754
        kluisnummer = kluisinfo[0]
        kluisnummers.remove(int(kluisnummer))

    if len(kluisnummers) > 0 :
        nieuwe_code = input("Geef een kluiscode op: ")
        nieuw_nummer = kluisnummers[0]

    outfile = open('kluizen.txt', 'a')
    outfile.write(str(nieuw_nummer) + ";" + nieuwe_code)
    outfile.close()




    print(regels)

#functie 1
def aantal_kluizen():
    kluisnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(kluisnummers)

#functie 3
def ophalen():
    kluisnummer1 =  input("wat is uw kluisnummer")
    toegangscode = input("Wat is uw toegangscode")

    infile = open("kluizen.txt")
    regels = infile.readlines()

    for regel in regels:
        #mogelijke waarde kan zijn 11:6754
        kluisinfo = regel.split(";")
        # wordt dan 11, 6754
        kluisnummer = kluisinfo[0]

    for lijn in regels
         kluisnummer





    print(regels)
    infile.close()





print("1. Ik wil weten hoeveel kluizen nog vrij zijn")
print("2. IK wil een nieuwe kluis")
print("3. Ik wil even iets uit mijn kluis halen")
print("4. Ik geef mijn kluis terug")
print()
optie = input("Welkom, voor uw keuze in: ")

if optie == "1":
    print('Uw keuze is 1')
    aantal_kluizen()
elif optie == "2":
    print("Uw keuze is 2")
    nieuwe_kluis()
elif optie == "3":
    print("Uw keuze is 3")
    ophalen()
elif optie == "4":
    print("Uw keuze is 4")

else:
    print("Foute invoer")

