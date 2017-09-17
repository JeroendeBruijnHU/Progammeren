old_pw = (input("Voer uw huidige wachtwoord in"))
new_pw = (input("voor uw nieuwe wachtwoord in"))

if new_pw != old_pw and len(new_pw) >6 :

    print("True")



else:
    print("False")