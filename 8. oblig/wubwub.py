#Dette programmet tilsvarer main.py, men har et bestemt antall linjer og oppdateringer.
#Dette er utelukkende for morroskyld.

from spillebrett import Spillebrett

def main():
    spillebrett = Spillebrett(50, 200)
    spillebrett._generer()
    spillebrett.tegnBrett()
    drive = 1000
    while drive > 1:
        spillebrett.oppdatering()
        spillebrett.tegnBrett()
        drive -= 1
    #print("Generasjon: ", spillebrett._generasjonsnummer,
    #" - Antall levende celler: ", spillebrett.finnAntallLevende())
main()
