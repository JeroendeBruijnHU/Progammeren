maximaal_aantal_kluizen = 12

#functie 1 - Aantal kluizen vrij
def toon_aantal_kluizen_vrij():
    aantalkluizen = checkkluizen() #Wat uit functie 1.1 komt
    return (maximaal_aantal_kluizen - len(aantalkluizen))

#Functie 1.1, tussenfunctie
def checkkluizen():
    infile = open("kluizen.txt")
    kluizen = infile.readlines()
    newlist = []
    for ieder in kluizen:
       oldlist =  ieder.split(";") #verandert "11;6754" in "11" , "6574"
       newlist.append([int(oldlist[0]), oldlist[1]]) #voegt de twee waarden toe aan de nieuwe lijst
    infile.close()
    return newlist


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
        kluisnummer = kluisinfo[0] #wordt dus 11
        kluisnummers.remove(int(kluisnummer))

    if len(kluisnummers) > 0 :
        nieuwe_code = input("Geef een kluiscode op: ")
        nieuw_nummer = kluisnummers[0]

        outfile = open('kluizen.txt', 'a')
        outfile.write(str(nieuw_nummer) + ";" + nieuwe_code + "\n")
        outfile.close()
    print (regels)


#functie 3
def ophalen():
    kluizen = checkkluizen()
    kluisnummer1 =  int(input("wat is uw kluisnummer"))
    toegangscode = str(input("Wat is uw toegangscode"))
    #infile = open("kluizen.txt")
    #regels = infile.readlines()
    #infile.close()
    combinatie = [  int(kluisnummer1), str(toegangscode), "\n"]
    print(combinatie)
    print(kluizen)

    for regel in kluizen:
        if combinatie in kluizen:
            return "Access Granted"
        else:
            return "Access Denied"






print("1. Ik wil weten hoeveel kluizen nog vrij zijn")
print("2. IK wil een nieuwe kluis")
print("3. Ik wil even iets uit mijn kluis halen")
print("4. Ik geef mijn kluis terug")
print()
optie = input("Welkom, voor uw keuze in: ")

if optie == "1":
    print('Uw keuze is 1')
    print("Er zijn nog ",  toon_aantal_kluizen_vrij(),  "kluizen vrij")
elif optie == "2":
    print("Uw keuze is 2")
    print (nieuwe_kluis())
elif optie == "3":
    print("Uw keuze is 3")
    print(ophalen())
#elif optie == "4":
#    print("Uw keuze is 4")

else:
    print("Foute invoer")

