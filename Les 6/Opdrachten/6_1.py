maandnummer = input("Welk maandnummer is het?")
maandnummer = int(maandnummer)

if (maandnummer) > 0 and (maandnummer) < 3 :
    print("winter")

elif (maandnummer) >= 3 and maandnummer < 6:
    print("lente")

elif (maandnummer) >= 6 and maandnummer < 9:
    print("zomer")

elif (maandnummer) >= 9 and maandnummer < 12:
    print("Herfst")

if (maandnummer) == 12:
    print("winter")