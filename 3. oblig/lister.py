#1
'''Programmet lager en liste med tre verdier. Deretter blir en fjerde verdi lagt til
i programmet. Til slutt printes den første og tredje verdien i listen.'''

liste1 = [1, 5, 9]
liste1.append(11)
print(liste1[0], liste1[2])

#2
'''Programmet lager en tom liste. Deretter brukes .append og en input-funksjon
til å samle inn 4 input fra brukeren. Til slutt printes den ferdige listen.
Her har jeg gjort oppgaven to ganger, en gang med bruk av prosedyre, og en uten.
Var usikker på hva som var best, så jeg lot begge stå.(Jeg bruker liste3 videre i oppgavene)'''

liste2 = []
liste2.append(input("Skriv inn et navn(1/4): "))
liste2.append(input("Skriv inn et navn(2/4): "))
liste2.append(input("Skriv inn et navn(3/4): "))
liste2.append(input("Skriv inn et navn(4/4): "))
print(liste2)

liste3 = []
def navn():
    liste3.append(input("Skriv inn et navn(1/4): "))
    liste3.append(input("Skriv inn et navn(2/4): "))
    liste3.append(input("Skriv inn et navn(3/4): "))
    liste3.append(input("Skriv inn et navn(4/4): "))
navn()
print(liste3)

#3
'''For å forsikre at det ikke er tull med store og små bokstaver har jeg lagt inn en
funkjson som endrer alle verdiee i listen til små bokstaver. Deretter sjekker programmet om
navnet mitt finnes i lista ved bruk av if og else, og printer to forskjellige output om
det stemmer eller ikke.'''

liste3 = [navn.lower() for navn in liste3]
if 'kristian' in liste3:
    print("Du husket meg!")
else:
    print("Glemte du meg?")

#4
'''Programmet lager en ny liste der tallene fra liste1 førs adderes, så multipliseres, og lagres sammen.
Deretter printer programmet den nye listen med navn sum_prod.
Den opprinnelige liste1 og sum_prod legges sammen og danner kombi_liste, for å så printes.
Til slutt bruker programmet en .pop() funkjson til å fjerne den siste indexen i listen to ganger,
og printer sluttresultatet.'''

sum_prod = [liste1[0] + liste1[1] + liste1[2] + liste1[3] , liste1[0] * liste1[1] * liste1[2] * liste1[3]]
print(sum_prod)
kombi_liste = liste1 + sum_prod #, eller + ???
print(kombi_liste)
kombi_liste.pop(-1)
kombi_liste.pop(-1)
print(kombi_liste)
