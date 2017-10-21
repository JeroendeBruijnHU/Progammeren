import xmltodict


def lezen():
    with open("stations.xml") as bestand:
        stops = xmltodict.parse(bestand.read())

        print("Stations en Type : ")
        codes = ""
        types = ""

        for x in stops["Stations"]["Station"]:
            codes = (x["Code"])
            types = (x["Type"])
            print(codes, types)

        print("\n")

        print("Codes en Synoniemen")
        synoniemen = ""

        for y in stops["Stations"]["Station"]:
            if y["Synoniemen"]:
                synoniemen = (y["Synoniemen"]["Synoniem"])
                print(codes, synoniemen)

        print("\n")

        print("Lange namen:")
        lange_naam = ""
        for z in stops["Stations"]["Station"]:
            lange_naam = (z["Namen"]["Lang"])
            print(lange_naam)


lezen()