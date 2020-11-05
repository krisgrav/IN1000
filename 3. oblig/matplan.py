#1
matplan = {"Kari Helgesen" : ["Frokost: Toast og juice." ,
 "Lunsj : Yoghurt og eple." , "Middag: Biff stroganoff"] ,
 "Helge Simonsen" : ["Frokost: Frokostblanding med melk." ,
  "Lunsj: Rundstykke med ost." , "Middag: Lapskaus"]}

#2
def p1():
    navn = input("Hvilken beboer søker du etter? : ")
    if (navn.lower()) == "kari helgesen":
        print(matplan["Kari Helgesen"])
    elif (navn.lower()) == "helge simonsen":
        print(matplan["Helge Simonsen"])
    else:
        print("Dette navnet er ikke registrert.")
        forsok = input("Vil du prøve igjen?")
        if (forsok.lower()) == "ja":
            p1()
        else:
            print("Den er grei.")
p1()

#3
#a
'''Her ville jeg brukt en ordbok. Da har en muligheten til å lagre navn på studentene
som nøkkelverdi og brukernavn som mappeverdi slik at det er oversiktlig og mulig å
søke opp. Dette kan også gjøres med en liste eller mengde, men jeg tror det vil
bli ryddigere i en ordbok.'''
#b
'''Her ville jeg brukt nøsting med en ordbok og en liste. Navnene brukes som nøkkelverdi
og mappeverdien vil være en liste over brukernavn og tilhørende poeng.'''
c#
'''Til dette ville jeg brukt en mengde. Da kan alle nvnene skrives legges inn i
mengden ettersom flere personer vinner, og om noen skulle vinne to ganger
vil de allikevel bare telles en gang.'''
d#
'''Til dette ville jeg brukt en enkel liste over allergiene.
Om en ønsker å gjøre det mer komplisert kan en også lage en ordbok med matretter
som nøkkelverdi og de tilhørende allergenene som mappeverdi.'''
