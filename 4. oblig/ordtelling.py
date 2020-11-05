'''Først lager programmet en funkjson som teller antall bokstaver i et ord.
Deretter kaller programmet på funksjonen.'''

def funksjon1(tekst):
    return len(tekst)

funksjon1(input("Skriv inn et ord: "))

'''Programmet lager nok en funkjson. I funksjonen dannes jeg en ordliste som inneholder
en setning hvor hvor væt ord blir representert som et element i listen.
Deretter opprettese en tom ordbok, som blir fylt opp av en for loop. Nøkkelverdien
blir antall ganger ordet er å finne i setningen.'''

def funksjon2(setning):
    ordliste = setning.split()
    ordbok = {}
    for index in ordliste:
        ordbok[index] = ordliste.count(index)
    return ordbok

funk2 = funksjon2(input("Skriv inn en setning: "))
print(funk2)

'''Det dannes et program som tar inn en setning fra bruker, og printer antall ord i
setningen. Setningen legges så inn i en ordbok ved bruk av funksjonen fra oppgave 2.
Så brukes en for loop til å printe antall ganger ordene forekommer i setnigen,
etterfulgt av hvor mange bokstaver det er i hvert ord.'''

def program():
    setning = (input("Skriv inn en setning: "))
    liste1 = setning.split()
    print("Det er ", len(liste1), "ord i setningen.")
    ordbok = funksjon2(setning)
    for i in ordbok:
        print("Ordet", i, "forekommer", ordbok[i], "antall ganger i setningen.")
        print("Ordet", i, "har", funksjon1(i), "antall bokstaver.")
program()
