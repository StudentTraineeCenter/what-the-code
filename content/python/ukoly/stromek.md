# zeptáme se uživatele na počet pater
pocet = int(input("Zadej počet pater: "))

# vytvoření pater
for x in range(pocet):
    patro = "" # připravíme si proměnou pro patro(resetuje se při každém cyklu)
    patro += (pocet-x)*" " # přidáme odsazení patra od strany (přidá tolikrát string " ", dá se použít místo toho, abychom dělali for cyklus)
    patro += (x*2+1)*"*" # přidáme část stromu (přidá tolikrát string "*")
    print(patro) # vypíšeme aktuální patro stromu

# vytvoření kmenu
kmen = (pocet-1)*" " + "***"
print(kmen) # vypíšeme kmen