def code(invoerstring):
    nieuwestring = ""
    for letter in invoerstring: #waarom werkt dit niet? 
        stap1 = ord(letter) #vertaal "a" in 97
        stap2 = chr((stap1)+3 ) #voegt 3 bij de charachter waarde
        nieuwestring = nieuwestring + stap2

    return nieuwestring

print(code("RutteAlkmaarDen Helder"))