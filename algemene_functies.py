def mijn_functie_1(a, b, c, d):
    return a * a, b * b, c * c, d * d

totaal = mijn_functie_1(2, 4, 10, 12)
print(totaal)

def mijn_functie_2(a,b):
    uitvoer_lijst =[]
    uitvoer_lijst.append(a + b)
    uitvoer_lijst.append(a - b)
    uitvoer_lijst.append(a * b)
    uitvoer_lijst.append(a / b)
    return uitvoer_lijst
print(mijn_functie_2(12,3))
print(mijn_functie_2(12,2))
print(mijn_functie_2(10,5))
print(mijn_functie_2(100,20))