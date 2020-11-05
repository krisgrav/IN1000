#Klassen Celle opprettes, med en konstruktør der alle objektene får status doed fra start.

class Celle:
    def __init__(self):
        self._status = "doed" #0 = død, 1 = levende

# Metoden endrer status på celleobjektet til "doed".
    def settDoed(self):
        self._status = "doed"
        return self._status

# Metoden endrer status til "levende".
    def settLevende(self):
        self._status = "levende"
        return self._status

# Om cellen er levende il denne metoden returnere True
    def erLevende(self):
        if self._status == "levende":
            return True
        else:
            return False

# Denne metoden bruker .erLevende() til å sjekke status på en celle, og returnerer "O"
# om den er levende.
    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        else:
            return "."
