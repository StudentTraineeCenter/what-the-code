# Určení ročního období

## Zadání

Když už umíme rozlišit přestupný a nepřestupný rok, teď potřebujeme rozlišit roční obdbí, a když už jsme u toho tak i vypsat slovy dný měsíc.
Uživatel zadá číslo měcíse a program podle toho vypíše Měsíc a roční období.

## Ukázka

```
Zadej číslo měsíce 1-12: 3
Práve je Březen a je jaro.
```

## Řešení

```python
mesice = ["Leden","Únor","Březen","Duben","Květen","Červen","Červenec","Srpen","Září","Říjen","Listopad","Prosinec"]

mesic = int(input("Zadej číslo měsíce 1-12: "))

odpoved = "Právě je " + mesice[mesic-1] + " a je "

if mesic in [12, 1, 2]:
    print(odpoved + "Zima")
elif mesic in [3, 4, 5]:
    print(odpoved + "Jaro")
elif mesic in [6, 7, 8]:
    print(odpoved + "Léto")
elif mesic in [9, 10, 11]:
    print(odpoved + "Podzim")
else:
    print("Neplatný měsíc.")
```