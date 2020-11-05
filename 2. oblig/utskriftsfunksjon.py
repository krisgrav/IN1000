#1
'''I linje 5, og 6 danner programmet to variabler, navn og bosted, ved bruk av input.
Videre i linje 7 printer programmet ut variablene sammen med tilhørende tekst.'''

navn = input("Skriv inn navn: ")
bosted = input("Hvor kommer du fra?: ")
print("Hei,", navn ,"! Du er fra ", bosted)

#2
'''Følgende del av programmet definerer koden fra tidligere som en prosedyre
med navnet p1(). Deretter kjøres koden tre ganger etter hverandre i linje 18, 19 og 20.'''

def p1():
    navn = input("Skriv inn navn: ")
    bosted = input("Hvor kommer du fra?: ")
    print("Hei," + navn + "! Du er fra " + bosted)

p1()
p1()
p1()
