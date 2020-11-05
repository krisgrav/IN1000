'''Programmet lager variabelen minFil der tekstfilen tempuratur.txt åpnes.
Det lages også en tom liste. Programmet itererer så, via en for-løkke, over
elementene i listen, stripper de, og legger de ann i den tomme listen.
Til slutt printes listen.'''

minFil=open("temperatur.txt")
minListe = []

for linje in minFil:
    minListe.append(linje.strip())

print(minListe)

'''Funksjonen funksjon defineres med liste som parameter. Variabelen sum får en verdi.
En for-løkke brukes til å iterere gjennom listen for hver linje, og legger sammen
verdiene som lagres i variabelen sum. Sum deles på lengden av listen, og lagres som
variabeln snitt. Snitt returneres. Deretter kalles funksjonen med minListe som
argument, sammen med en passende tekst.'''

def funksjon(liste):
    sum = 0
    for linje in liste:
        sum += float(linje)
    snitt = sum / len(liste)
    return snitt
print("Gjennomsnittstempreaturen er", funksjon(minListe), "grader.")
