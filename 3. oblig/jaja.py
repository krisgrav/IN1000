'''Lag et program som inneholder en resturantmeny med flere retter. Lag en oversikt over allergener i de forskjellige rettene.
Brukeren skal ha mulighet til å se menyen, sjekke hvilke retter han kan spise, og se en oversikt over allergenene samlet.'''

'''Her har jeg laget en meny for resturanten samt oversikt over de forskjellge allergenene i matrettene.
Til dette har jeg valgt å bruke lister, og til slutt samlet listene i en ordbok.
I ordboken er matrettene nøkkelverdier, og listen over allergener er nøstet inn som mappeverdi.'''

meny = ["Indrefilet med saus og grønnsaker" , "Fiskesuppe" , "Vegetarburger"]
allergener_indrefilet = ["kjøtt" , "laktose" , "løk" , "soya" , "rotgrønnsaker"]
allergener_fiskesuppe = ["løk" , "skalldyr" , "laktose" , "fisk"]
allergener_veggis = ["sopp" , "løk" , "egg" , "laktose" , "gluten"]
meny_allergener = {"Indrefilet med soppsaus og grønnsaker" : allergener_indrefilet ,
 "Fiskesuppe" : allergener_fiskesuppe , "Vegetarburger" : allergener_veggis}

'''Prosedyren p1() skal fungere som en mulighet til å søke opp allergener i menyen,
og gi brukeren output på hvilke retter han ikke kan spise. Til dette bruker jeg en variabel
med input, og if/elif setninger til å sjekke om allergien er å finne i noen av rettene.
Jeg hadde håpet å få til en kode der programmet sjekket om variabelen var å finne i en av mappeverdiene,
og gav output om hvilken nøkkelverdi den ligger under, men dette klarte jeg desverre ikke denne gangen.
Prosedyeren er lang, så jeg håper jeg lærer en bedre måte å gjøre dette på senere i kurset.'''

def p1():
    allergi = input("Hva er du allergisk mot? : ")
    if (allergi.lower()) in allergener_indrefilet and allergener_fiskesuppe and allergener_veggis:
        print("Du kan ikke spise indrefilet, fiskesuppe eller vegetarbruger. De inneholder: ")
        print(allergener_indrefilet)
        print(allergener_fiskesuppe)
        print(allergener_veggis)
        print("Ta deg et glass vann.")
    elif (allergi.lower()) in allergener_fiskesuppe and allergener_indrefilet:
        print("Du kan ikke spise indrefilet eller fiskesuppe. De inneholder: ")
        print(allergener_indrefilet)
        print(allergener_fiskesuppe)
    elif (allergi.lower()) in allergener_indrefilet and allergener_veggis:
        print("Du kan ikke spise indrefilet eller vegetarburger. De inneholder: ")
        print(allergener_indrefilet)
        print(allergener_veggis)
    elif (allergi.lower()) in allergener_fiskesuppe and allergener_veggis:
        print("Du kan ikke spise fiskesuppe eller vegetarburger. De inneholder: ")
    elif (allergi.lower()) in allergener_indrefilet:
        print("Du kan ikke spise indrefilet. Den inneholder: ")
        print(allergener_indrefilet)
    elif (allergi.lower()) in allergener_fiskesuppe:
        print("Du kan ikke spise fiskesuppe. Den inneholder: ")
        print(allergener_fiskesuppe)
    elif (allergi.lower()) in allergener_veggis:
        print("Du kan ikke spise vegetarburger. Den inneholder: ")
        print(allergener_veggis)
    else:
        print("Du kan spise alt på menyen!")

'''Her har jeg lagt inn en prosedyre som skal fungere som selve programmet.
Her får brukeren opp alternativer og kan velge om han vil se menyen (menyen printes),
søke på allergener (prosedyren p1() kjøres), eller se alle allergenene (ordboken printes).
Om brukeren skriver feil får han muligheten til å prøve igjen, og prosedyren kjøres på nytt fra starten.
Det er også lagt inn en kode for å avlutte programmet.'''

def program1():
    hva = input("Hva ønsker du å gjøre? (Se meny, søk etter allergier, se alle allergener, avslutte) : ")
    if (hva.lower()) == "se meny":
        print(meny)
        program1()
    elif (hva.lower()) == "søk etter allergier":
        p1()
        program1()
    elif (hva.lower()) == "se alle allergener":
        print(meny_allergener)
        program1()
    elif (hva.lower()) == "avslutte":
        print("Ha en fin dag!")
        exit()
    else:
        print("Her skjedde det noe galt!")
        retur = input("Vil du prøve igjen?")
        if (retu.lower()) == "ja":
            program1()
        else:
            print("Den er grei!")

'''Prosedyren kjøres.'''

program1()
