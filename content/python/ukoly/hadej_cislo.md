# Uhodni číslo

## Zadání

Cílem je udělat program, kde se hráč snaží uhodnout číslo.
Hráč si vždy typne číslo, podle toho mu program řekne zda je dané číslo větší či menší než hledané.
Jakmile číslo uhodne, tak mu program řekne, jak dlouho mu to trvalo.

## Možný průběh

```
Hádej číslo mezi 1 a 100.
Kolik si myslíš?:50
víc
Kolik si myslíš?:75
víc
Kolik si myslíš?:83
víc
Kolik si myslíš?:90
víc
Kolik si myslíš?:95
víc
Kolik si myslíš?:98
víc
Kolik si myslíš?:99
Hurá. hádané číslo bylo 99. Trvalo ti to celých 7 pokusů.
```

## Řešení

```python
import random # připojení knihovny pro generování náhodného čísla

tajne = random.randint(1,100) # vygenerování náhodné čísla od 1 do 100

pokusy = 0

while True:
    cislo = int(input("Jaké číslo si myslíš:")) # hráč typne číslo
    if cislo < 1 or cislo > 100: # pokud je mimo rozsah, tak typne znovu
        print("Číslo neni v rozsahu od 1 do 100!")
        continue

    if cislo < tajne: # řekne jak je jeho číslo oproti hádanému
        print("Hádané číslo je větší!")
    elif cislo > tajne:
        print("Hádané číslo je menší!")
    else:
        print("Gratuluji, uhádl jsi číslo:" + str(tajne))
        print("Trvalo ti to " + str(pokusy) + "pokusů.")
        break
    pokusy += 1
```