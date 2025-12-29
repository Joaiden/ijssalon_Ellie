def presenteer(dictionary, totaal):
    for sleutel, waarde in dictionary.items():
        print(f"{sleutel} : {waarde} euro")

    print("==========================")
    print(f"totaal : {totaal} euro")