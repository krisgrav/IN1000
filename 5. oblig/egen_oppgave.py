'''Lag et program som kan brukes av skreddere for å lagre mål. Programmet skal kunne lagre
et ubegrenset antall mål, og også gjøre disse om fra cm til tommer.'''


'''Programmet starter med å lage en rekke lister og ordlister som skal brukes senere.
Listene er nøstet inn i ordbøkene.'''

'''Videre i programmet er det liten sammenheng før alt samles i hovedprogrammet
til slutt, sorry for det.'''

skulder_liste = []
hals_liste = []
liv_liste = []
skulder_liste_cm = []
hals_liste_cm = []
liv_liste_cm = []
skredder = {"Skulderbredde" : [skulder_liste], "Halsvidde" : [hals_liste], "Livvidde" : [liv_liste]}
skredder2 = {"Skulderbredde_cm"  : [skulder_liste_cm], "Halsvidde_cm" : [hals_liste_cm], "Livvidde_cm" : [liv_liste_cm]}

'''Prosedyren destinasjon1 er laget slik at brukeren kan velge hvilke mål som skal
føres inn, og hvor mange tall som skal føres inn. Valget står først mellom
skulder/hals/liv og deretter brukes en for-løkke med range bestemt av brukeren
til å ta imot verdier. Verdiene legges til valgt liste under riktig nøkkelverdi
i ordboken skredder.'''

def destinasjon1():
    hvor = input("Hvilke mål vil du legge til? (skulder, hals, liv): ")
    if (hvor.lower()) == "skulder":
        antall = int(input("Hvor mange tall vil du legge til?: "))
        for i in range(antall):
            tommer_verdi = float(input("Skriv inn lengde i tommer: "))
            skulder_liste.append(tommer_verdi)
    elif (hvor.lower()) == "hals":
        antall = int(input("Hvor mange tall vil du legge til?: "))
        for i in range(antall):
            tommer_verdi = float(input("Skriv inn lengde i tommer: "))
            hals_liste.append(tommer_verdi)
    elif (hvor.lower()) == "liv":
        antall = int(input("Hvor mange tall vil du legge til?: "))
        for i in range(antall):
            tommer_verdi = float(input("Skriv inn lengde i tommer: "))
            liv_liste.append(tommer_verdi)
    else:
        destinasjon()

'''Prosedyren destinasjon2 lar brukeren velge hvilke mål som skal regnes om til cm.
Når valget er tatt kalles funkjsonen tommerTilcm_3.(Jeg var innom en del varianter
av funkjsonen før jeg landet på denne, derav navnet.) Funksjonen har forskjellige
argumenter ettersom hva bukeren vil regne om. Funksjonen bruker argumentene liste
og slutt_liste avhengig av brukerens valg'''

def destinasjon2():
    hvor = input("Hvilke mål vil du regne om? (skulder, hals, liv): ")
    if (hvor.lower()) == "skulder":
        tommerTilcm_3(skulder_liste, skulder_liste_cm)
    elif (hvor.lower()) == "hals":
        tommerTilcm_3(hals_liste, hals_liste_cm)
    elif (hvor.lower()) == "liv":
        tommerTilcm_3(liv_liste, liv_liste_cm)
    else:
        destinasjon2()

'''Prosedyren intro skal være det første som møter brukeren. Har får den muligheten
til å legge til eller se data, og gjøre det om. Brukerens valg kaller på den
aktuelle prosedyren.'''

def intro():
    gjore = "1"
    while gjore != "4":
        gjore = input("Hva ønsker du å gjøre? 1 = Føre inn nye data. 2 = Se dine data. 3 = Tommer til cm. 4 = Avslutt: ")
        if gjore == "1":
            destinasjon1()
        elif gjore == "3":
            destinasjon2()
        elif gjore == "2":
            print(skredder)
            print(skredder2)
        elif gjore == "4":
            print("Ha en fin dag!")
            break
        else:
            intro()

'''Denne funksjonen skulle egentlig emd i programmet, men den brukes ikke.'''

def cmTiltommer(liste):
    for i in liste:
        ferdige_verdier.append(i / 2.54)
    print("Målene er", ferdige_verdier, "i tommer.")

'''Funksjonen tommerTilcm_3 defineres med parameterne liste og slutt_liste.
Deretter itererer den gjennom listen som blir sett som argument, og sender resultatet
til slutt_liste.'''

def tommerTilcm_3(liste, slutt_liste):
    for i in liste:
        slutt_liste.append(i * 2.54)
    print("Målene er", slutt_liste, "i centimeter.")

'''I hovedprogrammet er det hele samlet med passende tekst. Prosedyren intro, som inneholder
de forskjellige prosedyrene kalles. hovedprogrammet kalles.'''

def hovedprogram():
    print("Velkommen!")
    print("Dette programmet er designet for skreddere, for å holde kontroll på mål")
    print("og gjøre om fra tommer til cm.")
    intro()
hovedprogram()
