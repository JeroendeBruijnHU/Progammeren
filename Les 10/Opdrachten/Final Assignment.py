import xmltodict

def bewerken(bestand):
    with open(bestand) as stations:
        stops = stations.read()
        dictionary = xmltodict.parse(stops)
        return dictionary

lijststations = bewerken("stations.xml")
STATIONS = lijststations["Stations"]["Station"]

for x in STATIONS:
    print(x["Code"], x["Type"], x["Synoniemen"])





