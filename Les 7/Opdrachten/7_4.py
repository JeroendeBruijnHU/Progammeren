#Eerste functie - slaat company name en symbol op in dictionary
def ticker(filename):
    infile = open("symbols.txt")
    inhoud = infile.readlines()
    infile.close()
    tickerdictionary = {}

    for regel in inhoud: #bijvorobeeld yahoo : yhoo
        tickerinfo_list = regel.split(":")
        symbol = tickerinfo_list[1]
        companyname = tickerinfo_list[0]

        tickerdictionary[symbol] = companyname      # In deze regel voeg je waarde(companyname) toe aan sleutel(afkorting)
    return tickerdictionary


#Opdracht 1 - Linkt naam aan symbool
tickers = ticker("symbols.txt")
name = input("Enter company name")          #bijvoorbeeld yahoo

for item in tickers.items():                # Voor ieder item in tickers (bijv: YHOO:YAHOO GOOG:GOOGLE
    if item[1] == name:                     # Als compnayname gelijk is aan name = companyname (bijv: YAHOO - YAHOO
        print('Ticker symbol:' + item[0])   # print afkorting + eerste indexnummer van

#Opdracht 2 - Linkt symbool aan naam.
symbol = input("enter ticket symbol:")
print("companyname" + tickers[symbol])      # VALUE NAAR SLEUTEL