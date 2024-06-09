# Fibonačiho posloupnost

## Zadání

Program od uživatele přijme číslo a vypíše mu tolik členů Fibonačiho posloupnosti.
Fibonačiho posloupnost je taková, kde každé číslo je rovno součtu dvou předchozích.
Začítek posloupnosti: 1,1,2,3,5,8,13...

::show
## Řešení

```python
# zeptáme se uživatele na počet čísel
pocet = int(input("Zadej počet čísel:"))

# definujeme první dvě čísla pro počítání
cislo1 = 1
cislo2 = 0

for x in range(pocet):
    print(cislo1) # vypíšeme nejnovější číslo
    novy = cislo1 + cislo2 # zjistíme další číslo
    cislo2 = cislo1 # přepíšeme čísla pro počítání
    cislo1 = novy
```

Pokud bychom je chtěli vypsat na jeden řádek, museli bychom je postupně přidávat do listu ne stringu a ten pak na konci vypsat.

```python
# zeptáme se uživatele na počet čísel
pocet = int(input("Zadej počet čísel:"))

# definujeme první dvě čísla pro počítání
cislo1 = 1
cislo2 = 0

posloupnost = ""

for x in range(pocet):
    posloupnost += str(cislo1) + " " # přidáme nodé číslo do stringu
    novy = cislo1 + cislo2 # zjistíme další číslo
    cislo2 = cislo1 # přepíšeme čísla pro počítání
    cislo1 = novy

print(posloupnost)
```
::