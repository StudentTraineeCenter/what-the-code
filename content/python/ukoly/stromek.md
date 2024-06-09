# Vykreslení stromečku

## Zadání

Udělej program, kam uživatel zadá počet pater a podle toho se mu vykreslí stromeček do konzole.
Pro vykreslení stromečku se použijí `*`.
Každé patro stromečku je větší o jednu hvězdičku na každé straně.

## Ukázka

```
console: Počet pater? 5
    *
   ***
  *****
 *******
*********
   ***
```

::show
## Řešení

```python
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
```
::