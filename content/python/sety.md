# Sety

## Základní informace

Sety jsou neřazené soubory unikátních hodnot.

Vytváří se buď funkcí `set()` (do které můžeme vložit např. i řazený seznam (list))

```python
muj_set = set()
```

anebo výčtem hodnot oddělených čárkami a zaobalených v `{}`.

```python
muj_set = {"banan", "jablko"}
```

Hodnoty do něj přidáváme metodou `add()`
```python
muj_set.add("pomeranc")
print(muj_set)
```
```výsledek
Console: {'pomeranc', 'jablko', 'banan'}
```
a odebíráme metodou `remove()`
```python
muj_set.remove("banan")
print(muj_set)
```
```výsledek
Console: {'pomeranc', 'jablko'}
```

Všimli jste si, jak jsou hodnoty ve slovníku zpřeházené? To se děje, protože v setech na pořadí nezáleží a není v něm možné hodnoty hledat podle indexu - Python si tedy sety zobrazí, jak se mu zachce. 

A jelikož obsahují jen unikátní hodnoty, přidání dalšího pomeranče `muj_set` nijak nezmění.
```python
print(muj_set)
muj_set.add("pomeranc")
print(muj_set)
```
```výsledek
Console: {'pomeranc', 'jablko'} {'pomeranc', 'jablko'}
```



## Užitečné metody


Pokud máme set `set1 = {0,1,2,3}` a `set2 = {2,3,4,5}`, může se nám hodit zjistit, jaké hodnoty spolu sdílí
```python
print(set1.intersection(set2))
```
```výsledek
Console: {2, 3}
```

anebo jaké hodnoty `set1` má a `set2` nikoliv.

```python
print(set1.difference(set2))
```
```výsledek
Console: {0, 1}
```

Ke spojení dvou setů v jeden pak slouží metoda `union()`.

```python
print(set1.union(set2))
```
```výsledek
Console: {0, 1, 2, 3, 4, 5}
```
