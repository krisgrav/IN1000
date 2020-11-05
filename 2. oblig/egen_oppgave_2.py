'''Lag en quiz bestående av tre spørsmål. Av de tre spørsmålene skal et ha svaralternativer,
et spørsmål skal ta hensyn til feilmarginer, og et skal ha et konkret svar. Lag quizen slik at
brukeren har muligheten til å spille den på nytt etter første forsøk.'''

'''Programmet definerer første prosedyre, som inneholder spørsmål 1 i quizen.
Programmet ber om input a, b, eller c, og printer output til bruker etter som hva
hen svarer. I linje 18 tar programmet hensyn til feilskrivning, og kjører prosedyren
på nytt om ikke svaret er a, b, eller c.'''

def pros_1():
    spm_1 = input("Hvor ligger Norges lengste bro (a, b, eller c)? a: Drammen, b: Oslo, c: Bergen : ")
    if (spm_1.lower()) == "a":
        print("Riktig!")
    elif (spm_1.lower()) == "b":
        print("Feil.")
    elif (spm_1.lower()) == "c":
        print("Feil.")
    else:
        print("Der tror jeg du har en skrivefeil.")
        pros_1()

'''Programmet definerer prosedyre for spørsmål to. Programmet ber om en tallverdi fra brukeren
og lagrer ved hjelp fra int() inputen som en tallverdi. Programmet printer deretter ut
hvorvidt svaret  var riktig. Men om brukeren tar feil, men er innenfor en satt margin
1885 - 1900 får brukeren muligheten til å prøve på nytt. Dette står i linje 31 t.o.m 39.'''

def pros_2():
    spm_2 = int(input("Hvor mange meter er Norges lengste bro (oppgitt i heltall)? : "))
    if spm_2 == 1892:
        print("Riktig! Bra jobba!")
    elif spm_2 < 1900 and spm_2 > 1885:
        print("Feil, men du er veldig nær.")
        forsok = input("Vil du prøve igjen? : ")
        if (forsok.lower()) == "ja":
            pros_2()
        else:
            print("Da fortsetter vi!")
    else:
        print("Feil!")
        print("Da fortsetter vi!")

'''Programet definerer prosedyre for spørsmål 3. Her må brukeren svare helt nøyaktg for å få riktig.'''

def pros_3():
    spm_3 = input("I hvilken by ligger The Golden Gate Bidge? (Husk store bokstaver) : ")
    if (spm_3.lower()) == "san francisco":
        print("Riktig!")
    else:
        print("Feil, den ligger i San Francisco!")

'''Her kjører programmet hele quizen. Først printes en velkommen til brukeren, og hen får spørsmål om å starte.
Deretter kjøres prosedyrene (selv om brukeren vil eller ikke). Etter quizen får brukeren spørsmål om et nytt forsøk.
Svarer hen ja vil prosedyrene kjøres en andre gang.'''

print("Hei og velkommen til en bro-quiz om broer!")
klar = input("Er du klar? : ")
if (klar.lower()) == "ja":
    print("Da kjører vi på!")
    pros_1()
    pros_2()
    pros_3()
else:
    print("Jeg har dårlig tid, så vi starter uansett!")
    pros_1()
    pros_2()
    pros_3()

ny_start = input("Quizen er ferdig, har du lyst til å prøve en gang til? : ")
if (ny_start.lower()) == "ja":
    pros_1()
    pros_2()
    pros_3()
    print("Nå har du fått to forsøk, det får holde.")
else:
    print("Den er grei! Ha det bra.")

'''Jeg leste tilbakemeldingen fra forrige oblig om å bruke .lower() funksjonen først etter oppgaven,
så den ble skrevet inn etter programmet egt var ferdig.'''
