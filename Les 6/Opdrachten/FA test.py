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







print("1. Ik wil weten hoeveel kluizen nog vrij zijn")
print("2. IK wil een nieuwe kluis")
print("3. Ik wil even iets uit mijn kluis halen")
print("4. Ik geef mijn kluis terug")
print()
optie = input("Welkom, voor uw keuze in: ")

if optie == "1":
    print('Uw keuze is 1')
elif optie == "2":
    print("Uw keuze is 2")
    nieuwe_kluis()
elif optie == "3":
    print("Uw keuze is 3")
elif optie == "4":
    print("Uw keuze is 4")

else:
    print("Foute invoer")

