# Číselné datové typy - int a float

V téhle sekci se naučíme pracovat s číslami v Pythonu. Nejdřív si představíme oba základní číselné typy, načež si na nich vyzkoušíme několik užitečných operací.

## Typy čísel

Ačkoliv má Python různé "typy" čísel, zaměříme se na celá čísla (integers) a čísla s pohyblivou řádovou čárkou (floating point numbers).

Ne, jejich názvy se tě nesnaží nachytat - celá čísla jsou opravdu celá čísla a čísla s pohyblivou řádovou čárkou jsou opravdu čísla s desetinnou čárku (nebo zde spíš tečkou).

Příklady typů těchto čísel si můžeš prohlédnout v této tabulce:

| Číselný datový typ | Příklady|
|---|---|
| Celé číslo (integer) | -2, 0, 13414324134213 |
| Číslo s pohyblivou řádovou čárkou (floating point number) | -1.439, 1.0, 2e3 |

Tady tě může překvapit klasifikace čísla 1.0, protože se zdánlivě jedná o celé číslo. Python nicméně skutečně chápe jakékoliv číslo s *.0* na konci jako desetinné. Číslo zapsané jako 2e3 se pak rovná 2*10^3 a pro účely Pythonu 2000.0. Takže to je tedy jen další způsob značení čísel.

## Jednoduché výpočty

Sčítání:
```python
vypocet = 3+1
print(vypocet)
```
```výsledek
Console: 4
```

Odčítání:
```python
vypocet = 3-1
print(vypocet)
```
```výsledek
Console: 2
```

Násobení:
```python
vypocet = 3*2
print(vypocet)
```
```výsledek
Console: 6
```

Dělení
```python
vypocet = 3/2
print(vypocet)
```
```výsledek
Console: 1.5
```

Umocňování
```python
vypocet = 2**3
print(vypocet)
```
```výsledek
Console: 8
```

Odmocňování - pamatuj na to, že druhá odmocnina je to samé jako "půltá" mocnina:
```python
vypocet = 16**(1/2)
print(vypocet)
```
```výsledek
Console: 4
```

Dodržované správné pořadí matematických operací:
```python
vypocet = 3 + 3 * 4 - 3
print(vypocet)
```
```výsledek
Console: 12
```

```python
vypocet = (3 + 3) * (4 - 3)
print(vypocet)
```
```výsledek
Console: 6
```

## Zvláštnější výpočty

V Pythonu můžeme lehce spočítat i tzv. spodní celou část podílu (floor division), která nám řekne nejbližší celé číslo menší než podíl:
```python
vypocet = 5//2
print(vypocet)
```
```výsledek
Console: 2
```

Také dokážeme jedoduše zjistit zbytek po dělení operátorem modulo:
```python
vypocet = 5%2
print(vypocet)
```
```výsledek
Console: 1
```

## Shrnutí

| Operace | Operátor |
|---|---|
| Sčítání | + |
| Odčítání | - |
| Násobení | * |
| Dělení | / |
| Umocňování | ** |
| Spodní celá část podílu (floor division) | // |
| Zbytek po dělení (modulo) | % |
