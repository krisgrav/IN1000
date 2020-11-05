#Oppgave 3

#1
dag_1 = input("Skriv inn en dato med bruk av tall. Forst dag:")
maaned_1 = input(", deretter maaned.:")
dag_2 = input("Skriv så inn en annen dato. Forst dag:")
maaned_2 = input(", deretter maaned.:")
dato_1 = (dag_1 + maaned_1)
dato_2 = (dag_2 + maaned_2)

'''Her ber programmet brukeren om to datoer, og lagrer svarene som fire forskjellige
variabler, to for dag og to for måned. Det lager også to variabler der dag og måned
er slått sammen til en hel dato.'''

if maaned_1 < maaned_2:
    print("Riktig rekkefølge!")
if maaned_1 > maaned_2:
    print("Feil rekkefølge!")
elif maaned_1 == maaned_2 and dag_1 > dag_2:
    print("Feil rekkefølge!")
elif maaned_1 == maaned_2 and dag_1 < dag_2:
    print("Riktig rekkefølge!")
elif maaned_1 == maaned_2 and dag_1 == dag_2:
    print("Samme dato!")

'''Videre bruker programmet variabelene og if-statements til å sjekke hvilken av datoene som kommer først.
Er maaned_2 større enn maaned_1 vil "Riktig rekkefølge!" printes, men om det er omvendt vil "feil rekkefølge" printes.
Videre bruker programmet til linjer med elif i tilfellene der måneden er lik.
Linje 21 og 23 er skrevet slik at programmet først vil finne ut om variablene for
maaned_1 og maaned_2 er like, og deretter vurdere hvilken av dagene som kommer først,
for å gi to forskjellige svar i output. Er datoene like vil programmet i linjer
23 først se om måneden er lik, og deretter dag, før det da evt printer "samme dato!"'''
