cijferICOR = 6
cijferPROG = 7
cijferCSN = 8

gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3

beloningICOR = (cijferICOR * 30)
beloningPROG = (cijferPROG * 30)
beloningCSN = (cijferCSN * 30)
beloningtotaal = (cijferCSN + cijferICOR + cijferPROG)

overicht = ( 'Mijn Cijfers (gemiddeld een)' + str(gemiddelde) + 'leveren een beloning op van' + " €" +  str(beloningtotaal) )

print(overicht)