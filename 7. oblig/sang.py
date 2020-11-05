#Klassen Sang opprettes.
#I konstruktøren får instansvariablene _tittel og _artist verdi.
class Sang:
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._Artist = artist

#Denne metoden printer titel og artist på objektet med tilhørende tekst.
    def spill(self):
        print("Spiller:", self._tittel, "-", self._Artist)

#Denne metoden tar inn parameteren navn, og splitter den.
#Videre itterer metoden over de splittede delene, og bruker en if test til å
#sjekke om deler av navn finnes i self._Artist. Til slutt returneres false eller true.
    def sjekkArtist(self, navn):
        x = navn.split()
        for x in x:
            if x.lower() in self._Artist.lower():
                return True
        return False

#Denne metoden tar inn parameteren tittel, og sjekker om tittel er det samme som
#self._tittel. Om dette stemmer brueks en for løkke til å sjekke om deler av
#tittel er å finne i self._tittel, og returnerer true eller false.
    def sjekkTittel(self, tittel):
        x = tittel.split()
        if tittel.lower() == self._tittel.lower():
            return True
            for x in x:
                if x.lower() in self._tittel.lower():
                    return True
        return False

#Denne metoden sjekker først om tittel er det samme som self._tittel på samme måte som tidligere.
#Om dette stemmer sjekker den artist. Om begge to stemmer returneres true, ellers false.

    def sjekkArtistogTittel(self, artist, tittel):
        x = tittel.split()
        for x in x:
            if x.lower() in self._tittel.lower():
                y = artist.split()
                for y in y:
                    if y.lower() in self._Artist.lower():
                        return True
        return False
