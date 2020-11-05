#Klassen Sang importeres fra sang.
from sang import Sang

#_sanger og _navn dannes i konstruktøren til klassen Spilleliste.
class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

#Denne metoden leser inn en en fil med bruk av parameteren filnavn.
#Videre ittereres det over linjene i filen, og de legges til i listen
# _sanger en etter en.
    def lesFraFil(self, filnavn):
        data = open(filnavn)
        for linje in data:
            biter = linje.strip().split(";")
            self._sanger.append(Sang(biter[0], biter[1]))

#Denne metoden legger til parameteren nySang i listen _sanger.
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

#Denne metoden fjerner en sang fra listen _sanger.
    def fjernSang(self, sang):
        self._sanger.remove(sang)

#Denne metoden kaller på metoden spill() fra klassen Sang, og bruker den til å spille av
#paramteteren sang.
    def spillSang(self, sang):
        sang.spill()

#Denne metoden gjør det samme som den forrige, men her ittereres det over alle linjene
#i listen_sanger før .spill() kalles på. Alle sangene i listen printes etter tur.
    def spillAlle(self):
        for linje in self._sanger:
            linje.spill()

#Denne metoden itterer over _sanger. Den bruker metoden .sjekktittel() fra Sang.
#Hvis x finnes iblant sangtittlene returneres den.
    def finnSang(self, tittel):
        for x in self._sanger:
            if x.sjekkTittel(tittel):
                return x
        return None

#Denne metoden oppretter først en tom liste. Videre itterer den over _sanger.
#Metoden .sjekkArtist() fra Sang brukes til å sjekke om artistnavnet finnes i
#_sanger. Om dette stemmer legges sangen under navnet til i den tomme listen.
#Når alle sangene er sjekket returneres listen med sanger.
    def hentArtistUtvalg(self, artistnavn):
        sanger2 = []
        for x in self._sanger:
            if x.sjekkArtist(artistnavn):
                sanger2.append(x)
        return sanger2
