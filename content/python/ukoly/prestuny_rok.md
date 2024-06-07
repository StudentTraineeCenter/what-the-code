# Kontrola přestupného roku

## Zadání

První úkol je udělat program do které když zadáme rok, tak nám řekne zda je rok přestupný či nikoliv.
Přestupnost roku má tři pravidla: 
- když je rok dělitelný 4 je přestupný
- když je rok dělitelný 100 je nepřestupný
- když je rok dělitelný 400 je přestupný

## Ukázka

```
Zadej rok: 2004
Rok je přestupný.

Zadej rok: 2100
Rok je nepřestupný.

Zadej rok: 1986
Rok je nepřestupný
```

## Řešení

```python
rok = int(input("Zadej rok: "))

if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
    print("Rok je přestuný!")
else:
    print("Rok je nepřestupný!")
```