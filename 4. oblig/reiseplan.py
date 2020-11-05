'''Først oppretter jeg fire lister, tre tomme, og en siste som inneholder
de tre første listene.'''
steder = []
plagg = []
dato = []
reiseplan = [steder, plagg, dato]

'''Så oppretter jeg en loop der brukeren kan legge inn informasjon i listene 5 ganger.'''

for i in range(5):
    steder.append(input("Skriv inn et reisemål: "))
    plagg.append(input("Skriv inn et klesplagg: "))
    dato.append(str(input("Skriv inn en dato: ")))

'''Her printer programmet ut listen "reiseplan" ved bruk av en for loop.'''
for i in reiseplan:
    print(i)

'''Bukeren får mulighet til å få ut informasjon fra listene. Først hvilken av de
tre listene, deretter hvilket element i listen'''

i1 = int(input("Skriv inn et tall fra og med 0 til og med " + str(len(reiseplan)-1) + " :"))
i2 = int(input("Skriv inn et tall fra og med 0 til og med " + str(len(reiseplan[i1])-1) + " :"))
if i1 <= len(reiseplan)-1 and i2 <= len(reiseplan[i1])-1:
    print(reiseplan[i1][i2])
else:
    print("Ugyldig input!")

'''If sjekken gir brukeren tilbakemelding om det blir oppgitt input som ikke stemmer
overens med listene.'''
