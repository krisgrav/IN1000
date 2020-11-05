'''Programmet danner en funkjson som adderer to tall og returnerer summen.'''

def adder(tall1, tall2):
    sum = tall1 + tall2
    return sum

'''Funkjsonen kalles to ganger med forskjellige arguemnter, og printer ut resultatet.'''

print("Summen av 13 og 22 er" , str(adder(13, 22)),".")
print("Summen av 69 og 420 er" , str(adder(69, 420)),".")

'''Programmet ber bruekren om tekst og bokstav som blir lagret som variabler.
Deretter dannes en funksjon med disse variabelene som parametere.'''

minTekst = input("Skriv en kort setning :")
minBokstav = input("Skriv en bokstav :")

def tellForekomst(minTekst, minBokstav):
    forekomst = minTekst.count(minBokstav)
    return forekomst

'''Programmet teller hvor mange ganger bokstaven forekommer i setningen ved bruk
av .count og returnerer resultatet.'''

print("Bokstaven forekommer", str(tellForekomst(minTekst, minBokstav)), "gang(er) i setningen.")
