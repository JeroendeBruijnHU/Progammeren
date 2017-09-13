loon = input('Wat verdien je per uur?')
uren = input('Hoeveel uur heb je gewerkt?')
loon = eval(loon)
uren = eval(uren)
geld = (loon * uren)

salaris = str(uren) + ' uur werken levert ' + str(geld) + ' op'
print (salaris)