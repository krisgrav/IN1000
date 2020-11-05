'''Programmet tar inn input fra brukeren helt til verdien 0 blir oppgitt, dette
skjer ved bruk av en while loop. Tallen legges inn i en tom liste.'''

tall = int(input("Skriv inn et tall :"))
liste = []
while tall != 0:
    liste.append(tall)
    tall = int(input("Skriv inn et tall :"))

'''Programmet printer så ut alle elementene i listen ved bruk av en for loop.'''

for x in liste:
    print(x)

'''For loopen går gjennom listen og adderer, oppdaterer listen, adderer for alle
elementene i listen før summen printes.'''

minSum = 0
for x in liste:
    minSum = minSum + x
print("Summen av listen er :", minSum)

'''To nesten identiske for loops går igjennom alle elementene i listen til de ha funnet
den laveste og høyeste tallverdien, og printer denne.'''

minst = liste[0]
for x in liste:
    if x < minst:
        minst = x
print("Det minste tallet i listen er :", minst)

storst = liste[0]
for x in liste:
    if x > storst:
        storst = x
print("Det største tallet i listen er :", storst)
