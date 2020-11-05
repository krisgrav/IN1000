#Oppgave 2
#2

'''Dette programmet starter med å spørre brukeren om hen vil ha en brus. Verdien som hentes inn fra brukeren
(ja eller nei) blir til variabelen "brus".'''

brus = input("Vil du ha en brus? (Ja/Nei): ")

if brus =="ja":
    print("Her har du en brus!")
elif brus =="nei":
    print("Den er grei!")
else:
    print("Det forstod jeg ikke helt.")

'''Etter input fra brukeren vil brogrammet gi tre mulige utfall. Svarer brukeren ja vil en setning skrives ut som output.
Svarer derimot brukeren nei vil en annen setning skrives. Til slutt er det skrevet en kode
med formål å dekke feilsvar og feilskrivning. Om noe som helst annet enn "ja" eller "nei" skrives
vil en tredje setning skrives ut.'''
