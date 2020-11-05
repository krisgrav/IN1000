'''Programmet henter klassen Motorsykkel fra filen med samme navn.'''

from motorsykkel import Motorsykkel

'''I hovedprogrammet opprettes tre objekter av klassen Motorsykkel.
Deretter printes de tre objektene ved metoden skrivUt fra klassen.
Den tredje motorsykkelen får oppdatert kmStand med 10 kilometer.
Deretter printes den nye kilometerstanden på sykkel3 med metode fra Klassen
Motorsykkel.'''

def hovedprogram():
    sykkel1 = Motorsykkel("Honda", "KN69420", 83142)
    sykkel2 = Motorsykkel("Yamaha", "WE34256", 120475)
    sykkel3 = Motorsykkel("Kawasaki", "DP18811", 55430)
    sykkel1.skrivUt()
    sykkel2.skrivUt()
    sykkel3.skrivUt()
    sykkel3.kjor(10)
    print("Ny kilometerstand:", sykkel3.hentKilometerstand())

'''hovedprogrammet kalles'''
hovedprogram()
