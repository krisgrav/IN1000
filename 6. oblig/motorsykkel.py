#Klassen Motorsykkel opprettes, med en kostruktør som har instansvariablenene
#merke, regNr og kmStand.
class Motorsykkel():
    def __init__(self, merke, regNr, kmStand):
        self._merke = merke
        self._regNr = regNr
        self._kmStand = kmStand

#Metoden kjor tar den aktuelle motorsykklen og en verdi for km som parameter.
#Så oppdaterer den kmStand ved å legge til den gitte km-verdien.

    def kjor(self, km):
        self._kmStand += km

#Denne metoden returnerer variabelen kmStand for den aktuelle motorsykkelen.

    def hentKilometerstand(self):
        return self._kmStand

#Denne metoden printer ut variablene for den aktuelle motorsykkelen med relevant tekst.

    def skrivUt(self):
        print("Merke:" + self._merke)
        print("Registreringsnummer: " + self._regNr)
        print("Kilometerstand:", self._kmStand)
