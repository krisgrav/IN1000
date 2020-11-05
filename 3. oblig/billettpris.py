# 1, 2, 3, 4, 5
'''Programmet definerer prosedyren bp(). I prosedyren dannes variabelen alder ved bruk av input fra brukeren.
Variabelen billettpris er satt til 0. Dersom brukeren er 17 år eller yngre oppdateres variabelen billettpris
til 30, og brukeren får printet ut output der prisen for den aktuelle billetten er endret til 30 kroner.
Videre følger elif for alder mellom 17 og 63, der prisen oppdateres og brukeren får output.
Til slutt i prosedyren er det brukt else for å dekke alle som ikke går under de to foregåede kategoriene.
Prosedyren kjøres fire ganger.'''

def bp():
    alder = int(input("Hvor gammel er du (år)? : "))
    billettpris = 0
    if alder < 17 or alder == 17:
        billettpris = 30
        print("Billettprisen for barnebillet er ", billettpris ," kroner.")
    elif alder > 17 and alder < 63:
        billettpris = 50
        print("Billettprisen for voksenbillett er ", billettpris ," kroner.")
    else:
        billettpris = 35
        print("Billettprisen for pensjonistbillett er ", billettpris ," kroner.")
bp()
bp()
bp()
bp()

'''Her er en prosedyre som gir samme output som bp(), men her brukes ikke en egen variabel for billettpris.'''

def bp2():
    alder = int(input("Hvor gammel er du (år)? : "))
    if alder < 17 or alder == 17:
        print("Billettprisen for barnebillet er 30 kroner.")
    elif alder > 17 and alder < 63:
        print("Billettprisen for voksenbillett er 50 kroner.")
    else:
        print("Billettprisen for pensjonistbillett er 35 kroner.")
