# Cykly

Z tomhle modulu si ukážeme, jak se v pythonu vytváří cykly.

## Dělení

Cykly slouží k pro opakování stejných operací.

Cykly se děli na dva druhy 
- `while`
  - vykonávají se, dokud je splněna podmínka
- `for`
  - vykoná se tolikrát, kolikrát řekneme

Tady si ukážem while cykly

## Použití

Stejně jako u podmínek, to že něco patří do cyklu python rozlišuje odsazením

Proto syntaxe cyklu vypadá takto:
```python
kód

while podmínka:
  udělej něco
  udělej něco

další kód
```
> jakmile odsazení skončí, tak to je konec obsahu cyklu a zbytek kódu se vykoná až poté, co cyklus skončí

Třeba pokud bychom chtěli zvětšovat proměnou x dokud nebude větší než 5 a vždy ji vypsat
```python
x = 1
while x < 5:
  print(x)
  i += 1
```
```
conzole: 1
         2
         3
         4
```
> Pokud chceme zvyšovat nějakou propměnou musíme ji nastavit před cyklem, jinak by se při každém opakování nastavila na stejnou hodnotu
> stejně tak, pokud vytvoříme nějakou proměnou v rámci cyklu, bude platit pouze pro daný cyklus, a pak zmizí

## Ukončení cyklu

Cyklus můžeme ukončit několika způsoby.

Jedním z nich je, že podmínka přestane platit.

Další možností je použítí `break`, který ukončí cyklus, i když podmínka stále platí

```python
x = 1
while x < 5:
  print(x)
  if x == 3:
    break
  x += 1
```
```
conzole: 1
         2
         3
```
> do cyklu jsme přidali podmíky, pokud se x = 3 tak skonči

Další možností je `continue`, který neukončí celý cyklus, ale pouze daný opakování a rovnou přejde k dalšímu
```python
x = 0
while x < 5:
  x += 1
  if x == 3:
    continue
  print(x)
```
```
conzole: 1
         2
         4
```
> tíme že nejprve zvýšíme x pak ho teprve vypíšem, tak můžeme vidět, že jsme přeskočili vypsání čásla 3

## Použití else

Jelikož ve `while` používáme podmínku, můžeme za něj stejěn jako v `if` přidat else:
```python
x = 1
while x < 5:
  print(x)
  i += 1
else:
  print("x je moc velký")
```
```
conzole: 1
         2
         3
         4
         x je moc velký
```
> else se vykoná pouze pokud podmínka už neni pravdivá
> pokud cyklus skončí pomocí break, tak se else část neprovede

## Nekonečný cyklus

Nekonečný cyklus vytvoříme tím, že nastavíme podmínku, kterou nemůže nikdy splnit

Další možností je, že místo podmínky napíšeme `True`

```python
x = 1
while True:
  print(x)
  i += 1
```
```
conzole: 1
         2
         3
         4
         ...
```
> na nekonečné cykly si musíme dávat pozor, jelikož jakmile je spustíme, tak se nedají zastavit
> Pokud se vám povede podobný cyklus spustit, běžtě do správce úloh a vypněte ho

## úkoly na procvičení

### Uhodni číslo

Úkolem je udělat hru, kde uživatel musí uhádnout číslo. Vždy se ho zeptáme na typ a řekneme mu, zda je číslo větší, či menší než hádané číslo.

Jakmile uživatel číslo uhádne, tak mu pragram napíše, kolik pokusů mu to trvalo.

Možný průběh:
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

[řešení](/content/python/ukoly/hadej_cislo.md)

### Šibenice

Druhým úkolem je udělat hru šibenice. Kde hráč vždy zadá písmeno a pokud je v hádaném slově, tak se zobrazí. Pokud to chcete udělat těžší, můžete přidat omezený počet životů.

Možný průběh:
```
Hádej slovo:
----
Máš 5 životů.
Zadej písmeno: e
-e--
Zadej písmeno: a
-e--
Už máš jen 4 životy.
Zadej písmeno: s
-es-
Zadej písmeno: a
-es-
Už máš jen 3 životy.
Zadej písmeno: t
test
Gratuluji, uhádl jsi slovo test. Zbylé životy: 3.
```

[řešení](/content/python/ukoly/sibenice.md)