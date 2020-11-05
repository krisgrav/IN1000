#1
'''Programmet danner en ordbok med matvarene og prisene fra oppgaveteksten. Deretter printes ordboken.'''
vare_pris = {'Melk' : 'kr 14,90,-' , 'Brød' : 'kr 24,90,-' , 'Yoghurt' : 'kr 12,90,-' , 'Pizza' : 'kr 39,90,-'}
print(vare_pris)

#2
'''Her ber programmet om input fra brukeren om navn på ny vare, og pris. Variablene legges deretter inn i ordboken.
Dette er definert som en prosedyre, og kjøres to ganger. Til slutt printer programmet ordboken, som nå inneholder to nye matvarer og priser.'''
def p1():
    ny_vare1 = input("Hvilken vare vil du legge til? : ")
    ny_pris1 = input("Hva koster varen? : ")
    vare_pris[ny_vare1] = ny_pris1
p1()
p1()
print(vare_pris)
