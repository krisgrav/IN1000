steder = []
plagg = []
dato = []
reiseplan = [steder, plagg, dato]

for i in range(5):
    steder.append(input("Skriv inn et reisemål: "))
    plagg.append(input("Skriv inn et klesplagg: "))
    dato.append(str(input("Skriv inn en dato: ")))

for i in reiseplan:
    print(i)



i1 = int(input("Skriv inn et tall fra og med 0 til og med " + str(len(reiseplan)-1) + " :"))
i2 = int(input("Skriv inn et tall fra og med 0 til og med " + str(len(reiseplan[i1])-1) + " :"))
if i1 <= len(reiseplan)-1 and i2 <= len(reiseplan[i1])-1:
    print(reiseplan[i1][i2])
else:
    print("Ugyldig input!")
