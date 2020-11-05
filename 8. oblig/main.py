#Klassen Spillebrett importeres.

from spillebrett import Spillebrett

#Hovedprogrammet dannes med passende tekster. Input brukes til å bestemme antall
#Rader og kolonner. Spillebrettet dannes og tegnes som output, sammen med generasjonsnummer og antall levende celler.

#Dette plasseres i en while-loop som ikke stopper før brukeren gir q som input.

def main():
    print("Hei!")
    rader = int(input("Hvor mange rader ønsker du?: "))
    kolonner = int(input("Hvor mange kolonner ønsker du?: "))
    spillebrett = Spillebrett(rader, kolonner)
    spillebrett._generer()
    spillebrett.tegnBrett()
    print("Generasjon: ", spillebrett._generasjonsnummer,
    " - Antall levende celler: ", spillebrett.finnAntallLevende())
    fortsett = ""
    while fortsett != "q":
        fortsett = input("Press enter for aa fortsette, eller q så enter for å avslutte: ")
        spillebrett.oppdatering()
        spillebrett.tegnBrett()
        print("Generasjon: ", spillebrett._generasjonsnummer,
        " - Antall levende celler: ", spillebrett.finnAntallLevende())
main()
