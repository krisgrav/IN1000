#Importerer randint fra random modulen, og klassen Celle fra celle.

from random import randint
from celle import Celle

# Klassen Spillebrett opprettes. Konstruktøren innehar instnasvariabler for rader,
# kolonner, rutenett og en generasjonsnummer.
class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = self._generer()
        self._generasjonsnummer = 0

# Denne metoden lager rutenettet som skal brukes til Game of Life.
# Den itererer over det oppgitte antallet rader, og med en nøstet liste får hver rad et gitt antall kolonner.
# Randint brukes når et nytt celleobjekt dannes, og gir cellen 1/3 sjanse for å være levende.
# Den nyopprettede cellen legges inn på riktig plass i rad/kolonne, og loopen hopper videre til neste
# "tomme" rute i rutenettet.
    def _generer(self):
        rutenett = []
        for j in range(self._rader):
            rutenett.append([])
            for i in range(self._kolonner):
                #rutenett[j].append(Celle())
                giStatus = randint(0, 2)
                nycelle = Celle()
                if giStatus == 0:
                    #objekt = Celle().settLevende()
                    #rutenett[j].append(Celle().settLevende())
                    nycelle.settLevende()
                rutenett[j].append(nycelle)
        return rutenett

# Denne metoden skriver ut rutenettet på en ordnet måte, og bruker metoden hentStatusTegn()
# til å gi alle objektene et grafisk tegn i rutenettet.
    def tegnBrett(self):
        for linje in self._rutenett:
            streng = ""
            for objekt in linje:
                streng += objekt.hentStatusTegn()
            print(streng)

# Denne metoden finner naboer hos en bestemt celle og lagrer de i en liste.
    def finnNabo(self, rad, kol):
        naboer = []
        for j in range(-1, 2): #Finner naboer på raden før, samme rad eller raden etter.
            for i in range(-1, 2): #Finner naboer på kolonnen før, samme eller etter.
                naboRad = rad + j
                naboKol = kol + i
                gyldig = True #Variabelen gyldig får verdien True.
                if naboRad == rad and naboKol == kol: #Denne linjen utelukker det objektet vi sjekker naboene til.
                    gyldig = False
                if naboRad >= self._rader or naboRad < 0: #Sjekker at det er en rad som finnes.
                    gyldig = False
                if naboKol >= self._kolonner or naboKol < 0: #Sjekker at det er en kolonne som finnes.
                    gyldig = False
                if gyldig:
                    naboer.append(self._rutenett[naboRad][naboKol]) #Hvis kriteriene stemmer legges objektet til i nabolisten med bruk av indeksene for rad og kolonne.
        return naboer #Listen returneres

#Denne metoden oppdaterer spillebrettet etter gitte regler.
#Først itereres det over alle objektene i rutenettet. Det lages en liste over naboer for alle objektene.
#Deretter legges de levende naboene til i en egen liste. Reglene til Game of Life brukes til å bestemmme
#om naboen skal endres eller forbli slik den er, og de legges enten i skalDo eller skalLeve listen.
#Til slutt itereres det over objektene i skalDo og status endres til doed med bruk av metoden settDoed():
#Tilsvarende skjer med skalLeve. For hver oppdatering får også instansvariabelen generasjonsnummer + 1.

    def oppdatering(self):
        skalDo = []
        skalLeve = []
        for rad in range(len(self._rutenett)):
            for kol in range(len(self._rutenett[rad])):
                naboliste = self.finnNabo(rad, kol)
                levendeNaboer = []
                for objekt in naboliste:
                    if objekt.erLevende():
                        levendeNaboer.append(objekt)
                antallLevende = int(len(levendeNaboer))
                if self._rutenett[rad][kol].erLevende() and antallLevende in range(2, 4):
                    skalLeve.append(self._rutenett[rad][kol])
                elif self._rutenett[rad][kol] and antallLevende == 3:
                    skalLeve.append(self._rutenett[rad][kol])
                else:
                    skalDo.append(self._rutenett[rad][kol])
        for x in skalDo:
            x.settDoed()
        for x in skalLeve:
            x.settLevende()
        self._generasjonsnummer += 1

#Denne metoden går igjennom alle objektene i rutenettet, og bruker en teller til
#å returnere antall levende celleobjekter.
    def finnAntallLevende(self):
        teller = 0
        for rad in range(len(self._rutenett)):
            for kol in range(len(self._rutenett[rad])):
                if self._rutenett[rad][kol].erLevende():
                    teller +=1
        return teller
