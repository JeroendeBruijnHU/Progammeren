studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    antw = []
    for student in studentencijfers:
        x = sum(student) / len(student)
        antw.append([x])
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    totaal = 0
    for student in studentencijfers:
        subtotaal = sum(student) # = totaal per student (243)
        aantal_cijfers = len(student)

        totaal = totaal + (subtotaal / aantal_cijfers)
    return totaal / len(studentencijfers)

def gem_alle_studenten(studentencijfers):
    alle_gemiddelden = gemiddelde_per_student(studentencijfers)
    return sum(alle_gemiddelden) / len(alle_gemiddelden)

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))







        #student1 = sum(studentencijfers[0])
#student2 = sum(studentencijfers[1])
#student3 = sum(studentencijfers[2])
#student4 = sum(studentencijfers[3])
#aantstudent1 = len(studentencijfers[0])
#aantstudent2 = len(studentencijfers[1])
#aantstudent3 = len(studentencijfers[2])
#aantstudent4 = len(studentencijfers[3])
#aantotaal = aantstudent1 + aantstudent2 + aantstudent3 + aantstudent4
#subtotaal = student1 +  student2 + student3 + student4
#gemiddelde = subtotaal / aantotaal






#print(gemiddelde_per_student(studentencijfers))