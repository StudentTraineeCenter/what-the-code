# zeptáme se uživatele na počet pater
pocet = int(input("Zadej počet pater: "))

# vytvoření pater
for x in range(pocet):
    patro = "" # připravíme si proměnou pro patro(resetuje se při každém cyklu)
    for i in range(pocet-x): # přidáme do patra odsazení
        patro += " "
    for i in range(x*2+1): # přidáme část stromu
        patro += "*"
    print(patro) # vypíšeme aktuální patro stromu

# vytvoření kmenu
kmen = ""
for x in range(pocet - 1): # vytvoříme odsazení pro kmen
    kmen += " "
kmen += "***"
print(kmen) # vypíšeme kmen