import xmltodict

def bewerken(file):
    with open(file) as artikelen:
        content = artikelen.read()
        xmldict = xmltodict.parse(content)
        return xmldict

artikeldictinary = bewerken("artikelen.xml")
ARTIKELEN = artikeldictinary["artikelen"]["artikel"]

for x in ARTIKELEN:
    print(x["naam"])