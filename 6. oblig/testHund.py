from hund import Hund

# klassen Hund importeres fra hund.py.
# Et hovedprogramm defieneres, og objektet hund1 dannes.
# Metoden spring kjøres tre ganger, og vekten printes med metoden hentVekt for hver gang.
# Metoden spis kalles to ganger med verdiene 2 og 3, og vekten printes for hver gang.

def hovedprogram():
    hund1 = Hund(6, 13)
    hund1.spring()
    hund1.hentVekt()
    hund1.spring()
    hund1.hentVekt()
    hund1.spring()
    hund1.hentVekt()
    hund1.spis(2)
    hund1.hentVekt()
    hund1.spis(3)
    hund1.hentVekt()

# Hovedprogrammet kalles.
hovedprogram()
