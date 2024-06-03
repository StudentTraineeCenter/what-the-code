# Cykly pokračování

V téhle části modulu si ukážeme cykly typu `for`

## použití

Cyklus `for` se používá pokud chceme projít list, tuple, slovník, string nebo určitý počet opakování.

Funguje tak, že když mu zadáme co má procházet, vykoná jeden cyklus pro každý element.

```python
list = ["jablko", "test", "pokus"]
for x in list:
  print(x)
```
> kde pro každý cyklus x bude mít hodnotu dat v listu na daném indexu
> index se pro každé opakování zvyšuje o jedna

### použití pro vypsání všech hodnot

Pro vypsání všech hodnot v listu

```python
list = ["červená","zelená","modrá"]
for x in list:
  print(x)
```
```
conzole: červená
         zelená
         modrá
```

Použití for pro string

```python
list = "test"
for x in list:
  print(x)
```
```
conzole: t
         e
         s
         t
```

Pokud ho chceme provést několikrát, potřebujeme funkci `range()`, do které se zadává kolikrát ho budeme chtít provést

```python
for x in range(5):
  print(x)
```
```
conzole: 0
         1
         2
         3
         4
```
> `Range()` vytvoří seznam čísel od `0` po číslo o jedno menší než naše

### předčesné ukončení

Stejně jako u while můžeme použít `break` pro ukončení nebo `continue` pro ukončení daného cyklu 

```python
for x in range(5):
  print(x)
  if x == 2
    break
```
```
conzole: 0
         1
         2
```

A stejně jako u while můžeme použít else na konci, pro vykonání kódu po ukončení cyklu

```python
for x in range(5):
  print(x)
else:
  print("úspěšně ukončeno")
```
```
conzole: 0
         1
         2
         3
         4
         úspěšně ukončeno
```

### jak řešit prázdno

For cyklus nemůže bít prázdný, takže pokud nechceme dávat žádné přákazy do cyklu, můžeme použít `pass`


```python
list = "test"
for x in list:
  print(x)
```
```
conzole: t
         e
         s
         t
```

### cyklus v cyklus v cyklu v ...

Cykly můžme vkládat i do sebe. Pak se nejprve vykoná celý vnitřní cyklus pak se přejde k další iteraci vnějšího cyklu.

```python
list = ["jablko", "jahoda", "mango"]
for x in range(3):
  for y in list:
    print(x, y)
```
```
conzole: 1 jablko
         1 jahoda
         1 mango
         2 jablko
         2 jahoda
         2 mango
         3 jablko
         3 jahoda
         3 mango
```

Stejné vkládání se dá dělat i u `while` cyklů a dají se i kombinovat

## úkoly na procvičení

### palindrom

Prvním úkolem je udělat program, kterému zadáme slovo/text, a napíše nám, zda se jedná o palindrom, nebo ne.

Palindrom je slovo/text, který je stejná ať ho čteme ze předu, či ze zadu

> příklad palindromu: "oko", "radar", "nepotopen"

[řešení](/content/python/ukoly/palindrom.py)

### fibonačiho posloupnost

Dalším úkolem je udělat program, kterému zadáme číslo, a on nám napíše tolik posobějdoucích čísel fibonačiho posloupnosti.

Fibonačiho posloupnost je taková, kde každé číslo je součtem dvou předchozích.

> začítek posloupnosti: 1,1,2,3,5,8,13...

[řešení](/content/python/ukoly/fibonaci_posloupnost.py)

### stromeček

Blíží se vánoce, a tak potřebujeme stromeček. Úkolem je udělat program, kde zadáme počet pater, a vykreslí nám do konzole stromeček.

možný výstup:
```
console: Počet pater? 5
    *
   ***
  *****
 *******
*********
   ***
```

[řešení](/content/python/ukoly/stromek.py)