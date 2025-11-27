from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro"
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    totaal_exclusief_btw = sum(inkomsten)
    totaal_inclusief_btw = (totaal_exclusief_btw * (1 + btw))
    return totaal_exclusief_btw, totaal_inclusief_btw
week_inkomsten = [220, 430, 125, 160, 205, 90, 345]
print(inkomsten_totaal(week_inkomsten, 0.09))

def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)
    return [hoogste, laagste]
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
print(laag_en_hoog(mijn_lijst))

def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    week_inkomsten = len(mijn_lijst)
    if week_inkomsten == 7:
        return totaal / week_inkomsten
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
print(f"de gemiddelde inkomsten deze week zijn {gemiddelde(mijn_lijst)}")

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
print(meervoudig(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print(combinatie([220, 430, 125, 160, 205, 90, 345]))