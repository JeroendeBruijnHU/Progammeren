def tellen(regels):
    infile = open("kaartnummers.txt")
    lijst = infile.readlines()
    return len(lijst)

def grootste(nummer):
    infile = open("kaartnummers.txt")
    lijst = infile.readlines()
    return max(lijst)





print("Dit bestand is ", tellen("kaartnummers.txt"), " regelslang")
print("Het grootste kaartnummer is", grootste("kaartnummers.txt")[0:6], "en dat staat op regel ") #hier moet nog index nummer