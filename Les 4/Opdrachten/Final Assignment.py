def standaardprijs(afstandKM):
    if afstandKM <= 0:
        prijs1 = 0

    if afstandKM <= (50):
        prijs1 = (afstandKM * 0.8)


    else:
        prijs1 = (afstandKM * 0.6) + 15.0


    return prijs1


def ritprijs(leeftijd, weekendrit, afstandKM):
    basisprijs = standaardprijs(afstandKM)

    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit == True:
            basisprijs = basisprijs * 0.65
        else:
            basisprijs = basisprijs * 0.7

    else:
        if weekendrit == True:
            basisprijs = basisprijs * 0.6

    return basisprijs


print(ritprijs(16, True, 40))