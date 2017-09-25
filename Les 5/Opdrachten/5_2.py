infile = open("kaartnummers.txt")

def splitten(inputregel):
    for regel in inputregel:
        waarde = regel.split (', ')
        print(waarde[1].strip(), "heeft als kaartnummer:", waarde[0].strip())

splitten(infile)
infile.close()
