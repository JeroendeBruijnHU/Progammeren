def rng(lijst):
    kleinste = min(lijst)
    grootste = max(lijst)
    bereik = grootste - kleinste
    return bereik

print(rng([4, 0, 1, -2]))


#list is een verwijzing
#integer maakt een kopie