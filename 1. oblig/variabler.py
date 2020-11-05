#Oppgave 1

#2
print("Hei student!")

'''Her vil programmet printe/skrive ut hva enn som er skrevet i parantes og anførselstegn.
Selv om input består av kode og tegn er det kun teksten i anførselstegn som vil vises i output.'''

#3
navn = input("Hva heter du? ")
print("Hei " + navn)

''' I linje 10 skrevet en input-kode som i output ber brukeren av programmet om
å oppgi navnet sitt i programmet. Navnet lagres som en variabel med navnet "navn".
I linje 11 skriver igjen programmet ut en tekst. Her printes teksten i
anførselstegn + variabelen "navn" fra linje 10.'''

#4
verdi_1 = 8
verdi_2 = 5

''' Her er det oppgitt to nye variabler som brukes senere i programmet.'''

#5
diff = (verdi_1 - verdi_2)
print("Differanse:", + diff)

''' I linje 24 dannes det en ny variabel med navnet "diff". I denne variabelen
har programmet regnet ut differansen mellom,de to variablene i linje 18 og 19.
Videre gir programmet en output til brukeren
bestående av tekst og variabelen "diff" fra linje 24.'''

#6
nytt_navn = input("Oppgi et nytt navn: ")
sammen = navn + nytt_navn
print(sammen)

'''Her ber programmet brukeren om å skrive inn et nytt navn, som igjen lagres som en
ny variabel. Videre lager programmet en variabel bestående av de to navnene fra tidligere,
og printer variabelen "sammen".'''

#7
sammen = navn + " og " + nytt_navn
print(sammen)

'''I denne delen av programmet blir variabelen "sammen" oppdatert slik at ordet
"og", og mellomrom skiller de to navnene. Til slutt printes de to navnene på nytt,
denne gangen adskilt med "og".'''
