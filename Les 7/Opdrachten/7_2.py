while True:
    woord = str(input("Geef een string van 4 letters"))
    if len(woord) != 4:
        print(woord, "heeft", len(woord), "tekens")

    else:
        break
print("Inlezen van Correcte string", woord, "is gelukt")