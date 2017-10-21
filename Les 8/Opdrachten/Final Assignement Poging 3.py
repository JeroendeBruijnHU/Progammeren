stations = ['Schagen','Heerhugowaard','Alkmaar','Castricum','Zaandam','Amsterdam Sloterdijk','Amsterdam Centraal','Amsterdam amstel','Utrecht Centraal',"'s-Hertogenbosch",'Eindhoven','Weert','Roermond','Sittard','Maastricht']

def inlezen_beginstation(stations):
    while True:
        begin = input("Geef het station waarvan u vertrekt")
        if begin in stations:
            print("U vertrekt vanaf", begin)
        if begin not in stations:
            print ("Foute invoer")

        else:
            break
    return stations.index(begin)

def inlezen_eindstation(stations,beginstation_index):
    while True:
        eind = input('Geef uw bestemming:')
        if eind in stations:
            print("Uw bestemming is")
        if eind not in stations:
            print("Foute Invoer")

        else:
            eind_index = stations.index(eind)
            if eind_index > beginstation_index:
                return stations.index(eind)
            else:
                print('Eindstation ligt voor beginstation')

def omroepen_reis(stations,beginstation_index,eindstation_index):
    print("Het beginstation",stations[beginstation_index],"is het",beginstation_index+1,"e station op het traject")
    print("Het eindstation",stations[eindstation_index],"is het",eindstation_index+1, "e station op het traject")

    print("De afstand bedraagt",(eindstation_index - beginstation_index),"station(s)")
    print('De prijs van het kaartje is',(eindstation_index - beginstation_index)*5,"euro","\n")
    print('Jij stapt in de trein in:',stations[beginstation_index])

    for x in stations[beginstation_index + 1:eindstation_index]:
        print('- ', x)
    print("Jij stapt uit de trein in:",stations[eindstation_index])


beginstation_index = inlezen_beginstation(stations)
eindstation_index = inlezen_eindstation(stations, beginstation_index)
omroepen_reis(stations,beginstation_index,eindstation_index)