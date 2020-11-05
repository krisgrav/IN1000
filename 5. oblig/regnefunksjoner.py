'''Her definerer jeg funkjsonen addisjon, og printer den med argumenter jeg har valgt
selv. I funkjsonen adderes tall1 og tall2 og summen av disse returneres.'''

def addisjon(tall1, tall2):
    sum_add = tall1 + tall2
    return sum_add
print(addisjon(4, 7))

'''Funkjsonene subtraksjon og divisjon er satt sammen på samme måte som addisjon.
Tall1 og tall2 trekkes fra hverandre eller deles, og resultatet lagres i sum_sub/divisjon
variablene. Resultatet returneres.'''

def subtraksjon(tall1, tall2):
    sum_sub = tall1 - tall2
    return sum_sub

def divisjon(tall1, tall2):
    sum_div = tall1 / tall2
    return sum_div

'''Her kalles subtraksjon og divisjon funkjsonene tre ganger hver, og uttrykket
assert brukes til å sjekke om verdien som er forventet stemmer med resultatet i funksjonen.
Om antagelsen stemmer vil det ikke skje noe, men om den er feil vil
"Svaret skal være ..." printes.'''


assert subtraksjon(15, 5) == 10, "Svaret skal være 10"
assert subtraksjon(-15, -5) == -10, "Svaret skal være -10"
assert subtraksjon(-15, 5) == -20, "Svaret skal være -20"

assert divisjon(20, 10) == 2, "Svaret skal være 2"
assert divisjon(-20, -10) == 2, "Svaret skal være 2"
assert divisjon(-20, 10) == -2, "Svaret skal være -2"

'''Her er funksjonen tommerTilcm definert med antallTommer som parameter.
Først brukes en assert-test til å sjekke om parameteren er større enn 0.
Om det stemmer vil variabelen cm få verdien av antallTommer * 2.54, og returnere
antall cm.'''

def tommerTilcm(antallTommer):
    assert antallTommer > 0
    cm = antallTommer * 2.54
    return cm
print(tommerTilcm(10))

'''Først defineres prosedyren skrivBeregninger. Deretter tar den inn to tall fra
bruker, og uttrykket float brukes i tilfelle input er flyttall.
Input lagres under variablene tall1 og tall2. Deretter brukes tall1 og tall2 som
argumenter i funksjonene addisjon, subtraksjon og divisjon, og resultatet printes.
Variabelen antallTommer får så en floatverdi via input, før den brukes i funkjsonen
tommerTilcm, og resultatet printes med passende tekst.
Prosedyren skrivBeregninger kalles på.'''

def skrivBeregninger():
    tall1 = float(input("Skriv inn tall 1: "))
    tall2 = float(input("Skriv inn tall 2: "))
    print("Resultatet av summering er :", addisjon(tall1, tall2))
    print("Resultatet av subtraksjon er :", subtraksjon(tall1, tall2))
    print("Resultatet av divisjon er : ", divisjon(tall1, tall2))
    print("Konvertering av tommer til cm:")
    antallTommer = float(input("Skriv inn et tall: "))
    print("Resultat: ", tommerTilcm(antallTommer))
skrivBeregninger()
