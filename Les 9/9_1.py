

try:
    aantal = int(input("Hoeveel man gaan er mee?"))
    kostenpp = 4356 / aantal
    if kostenpp <= 0:
        raise AssertionError
    print(kostenpp)

except ZeroDivisionError:
    print("Delen door 0 kan niet")

except AssertionError:
    print("Negatieve getallen zijn niet toegestaan") #werkt niet

except ValueError:
    print("Gebruik cijfers voor het invoeren van het aantal!")

except:
    print("Onjuiste invoer")



