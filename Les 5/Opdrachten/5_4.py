import datetime
#infile = open("hardlopers.txt", "w")
#infile.writelines("test")
#infile.close()

hardloper = input("Wat is je naam?")

infile = open("hardlopers.txt", "a")
#Voorbeeld: Thu 10 Mar 2016, 10:45:52, Miranda
vandaag = datetime.datetime.today()
x = vandaag.strftime("%a %d %b %Y %I:%M:%S %p")
infile.writelines(x + " " + hardloper + "\n ")

infile.close()


