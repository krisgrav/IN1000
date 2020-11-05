class Sang:
    def __init__(self, tittel, artist):
        self._tittel = tittel.lower()
        self._artist = artist.lower()

    def spill(self):
        print("Spiller", self._tittel, "-", self._artist)

    def sjekkArtist2(self, navn):
        if (navn.lower()) == self._artist:
            return True
        else:
            return False

    def sjekkArtist(self, navn):
        str(navn) in str(self.artist)


    def sjekkTittel(self, tittel):
        if (tittel.lower()) == self._tittel:
            return True
        else:
            return False

    def sjekkArtistogTittel(self, tittel, artist):
        if ((tittel.lower()) == self._tittel) and ((artist.lower()) == self._artist):
            return True
        else:
            return False
