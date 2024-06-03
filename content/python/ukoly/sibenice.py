import random # knihodna pro vytvoření náhodného čísla
# seznam slov ze kterých se vybírá
slova = ["test", "nevim", "strom", "sprej", "housenka", "expedice", "astronomie", "zmrzlina"]

tajne = slova[random.randint(0,len(slova)-1)] # vezme náhodné slovo ze seznamu

uhodnuto = len(tajne)*"_" # co má hráč uhádnuto, vytvoří string stejně dlouhý jako tajné
print("Hádej slovo:")

zivoty = 5 # vytvoříme životy

while zivoty != 0: # dokud hráči nedojdou životy
    print(uhodnuto)
    pismeno = input("Hádej písmeno:") # hrčč si typne písmeno
    uhadl = False # jestli se trefil, pokud ne, tak mu na konci ubereme život
    i = 0
    for x in tajne: # porovnáme typované písmeno se slovem
        if pismeno == x: # pokud se písmena shodují tak v uhádnuto nahradíme _ za dané písmeno
            uhodnuto = uhodnuto[:i] + x + uhodnuto[i+1:] # jelikož ve stringu nejde přepisovat přímo na indexu, musíme ho rozdělit a vložit písmeno mezi
            uhadl = True
        i += 1
    if uhadl:
        if tajne == uhodnuto: # pokud uhadl nové písmeno, zkontrolujeme, zda má celé slovo nebo ne
            print("Gratuluji, uhodl jsi slovo:" + uhodnuto)
            print("Zbylo ti: " + str(zivoty) + " životů!")
            break
    else: # pokud písmeno neuhádl ubereme život
        zivoty = zivoty - 1
        print("Špatně, už máš jen " + str(zivoty) + " životů!")
else:
    print("Bohužel ti došli životy :-(")
    


