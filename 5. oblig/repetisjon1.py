'''Den tomme listen mineOrd dannes.'''

mineOrd = []

'''Deretter defineres funksjonene slaaSammen og skrivUt. slaaSammen bruker parameterene
a og b, slår sammen disse to, og returnerer resultatet. skrivUt bruker en
for-løkke til å itterere gjennom en liste, og printe hver linje for seg selv.'''

def slaaSammen(a, b):
    sammen = a, b
    return sammen

def skrivUt(liste):
    for linje in liste:
        print(linje)

'''Her defineres prosedyren lokke(). Variabelen variabel1 får verdien "i".
En while-løkke brukes på variabel1, slik at den stopper om den får verdien "s".
Variabelen variabel1 får ny verdi gjennpm input. Er input "i" får brukeren skrive inn
to setninger, som legges sammen ved bruk av slaaSammen, og legges inn i listen mineOrd.
Er input "u" printes listen mineOrd. Om input er "s" stopper prosedyren.
Om brukeren skriver noe annet enn i, u eller s, får den beskjed
om at noe har gått galt, og prosedyren kalles igjen.'''

def lokke():
    variabel1 = "i"
    while variabel1 != "s":
        variabel1 = input("Skriv inn en bokstav (i/u/s): ")
        if (variabel1.lower()) == "i":
            a = input("Skriv inn en setning: ")
            b = input("Skriv inn en setning: ")
            mineOrd.append(slaaSammen(a, b))
        elif (variabel1.lower()) == "u":
            skrivUt(mineOrd)
        elif (variabel1.lower()) == "s":
            break
        else:
            nytt_forsok = input("Noe gikk galt, vil du prøve igjen? (ja/nei): ")
            if nytt_forsok == "ja":
                lokke()
            elif nytt_forsok == "nei":
                break
            else:
                break
'''Prosedyren hovedprogram dannes, og inneholder prosedyren lokke.
hovedprogram() kalles.'''

def hovedprogram():
    lokke()
hovedprogram()
