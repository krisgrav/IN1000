#1
'''Programmet danner variabelen for fahrenheit temp_fah.'''
temp_fah = 100
#2
'''Programmet printer variabelen temp_fah.'''
print(temp_fah)
#3
'''Programmet danner variabelen for celsius temp_cel.'''
temp_cel = (temp_fah - 32) * 5/9
#4
'''Programmet printer temp_cel.'''
print(temp_cel)
#5
'''Programmet oppdaterer variabelen temp_fah ved bruk av input fra bruker.
Verdien til temp_fah blir lagret som en tallverdi ved bruk av int().
Variabelen temp_cel oppdateres med den nye verdien fra temp_fah, og lagres også som en tallverdi.
Programmet printer variabeln temp_cel med tilhørende tekst.''' 
temp_fah = int(input("Skriv inn grader fahrenheit: "))
temp_cel = int((temp_fah - 32) * 5/9)
print("Det er ", temp_cel ,"grader celsius.")
