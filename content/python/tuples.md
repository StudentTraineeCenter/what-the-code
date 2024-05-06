# Tuples = neměnné uložení více hodnot do jendé proměnné

## Základní informace

tuples stejně jako listy slouží pro uložení více hodnot do jedné proměnné. Zapisují se stejně jako listy, ale na rozdíl od nich se zapisují do normálních závorek `()`.

Vytvoření tuple:
```python
tuple = (1, 2, 3)
print(tuple)
```
> Jednotlivé hodnoty jsou opět odděla `,`

Stejně jako listy, tuples jsou **řazený a indexovaný** (začíná se od 0), a díky tomu **umožňují duplikáty**

Po vytvoření jsou již **neměnné**, pokud tuple chceme upravit, musíme vytvořit nový.

Je možné vytvořit i tuple pouze pro jednu hodnotu:
```python
tuple = ("test",)
print(tuple)
```
> Musí tam být na konci `,`, jinak se nebude jednat o tuple

Stejně jako v listu, i v tuple můžou být hodnoty **různých datových typů**.

Pro zjištění délky(počtu hodnot) můžeme opět použít funkci `len()`

## Práce s tuples

Jelikož se stejně jako u listů jedná o řazený seznam, přístup a práce s hodnotami je velice podobná.

### Přístup k datům

Přístup k datům funguje stejně jako u listů, napíšeme název proměnné a do hranatých závorek index hodnoty, kterou chceme:

```python
tuple = (1, "test", True, 2, 2, "konec")
print(tuple[1])
```
```
conzole: test
```

### Měnění hodnot

Jelikož tuples jsou neměnné, naší jedinou možností, jak je změnit je vytvořit si list, založený na našem tuple a ten upravovat. Nakonec ho převedeme zpátky na tuple.

Pro práci s listy používáme metody, které jsme si ukázali v minulém modulu

Změna hodnoty:
```python
tuple = (1, "test", True, 2, 2, "konec")
list = list(tuple)
list[0] = 5
tuple = tuple(list)
print(tuple)
```
```
conzole: (5, "test", True, 2, 2, "konec")
```
> 1. Pomocí funkce `list()` vytvoříme list založený na našem tuple
> 2. Úpravy provedeme v listu
> 3. Nakonec funkcí `tuple()` přepíšeme předchozí tuple novým, založeným na aktuálním listu

### Přidání hodnot

Pro přidání hodnot použijeme stejný postup
```python
tuple = (1, "test", True, 2, 2)
list = list(tuple)
list.append("konec")
tuple = tuple(list)
print(tuple)
```
```
conzole: (1, "test", True, 2, 2, "konec")
```

Další možností jak přidat hodnoty do tuples je spojením tuples
```python
tuple1 = (1,2,3)
tuple2 = (4,5)
tuple = tuple1 + tuple2
print(tuple)
```
```
conzole: (1, 2, 3, 4, 5)
```
> Jelikož se jedná o spojení tuples, nebylo třeba převádět je na listy

Tuples se dají i násobit, pokud tuple vynásobíme, tolikrát se bude opakovat
```python
tuple1 = (1,2,3)
tuple = tuple1 * 2
print(tuple)
```
```
conzole: (1, 2, 3, 1, 2, 3)
```

### Odstranění hodnot

Odstranění jedné hodnoty:
```python
tuple = (1, "test", True, 2, 2, "konec")
list = list(tuple)
list.remove("konec")
tuple = tuple(list)
print(tuple)
```
```
conzole: (1, "test", True, 2, 2)
```

Nebo můžeme smazat celý list i s jeho proměnnou:
```python
tuple = (1, "test", True, 2, 2, "konec")
del tuple
```

### Rozbalení tuple

Procesu vytváření tuple se říká "zabalení hodnot" a proces rozbalení je přesný opak. Při rozbalení přiřadíme hodnoty z tuple proměnným.

```python
tuple = ("jahoda", "jablko", "banán")

(cervena, zelena, zluta) = tuple

print(zelena)
```
```
conzole: jablko
```
> Proměnné, ke kterým hodnoty chceme přiřadit dáme do závorek ve stejném pořadí, v jakém je chceme přiřadit.

Pokud chceme přiřadit více hodnot jedné proměnné, vytvoříme tím z dané proměnné list hodnot

Tohoto docílíme pomocí `*`
```python
tuple = ("jahoda", "banán", "jablko", "meloun")

(cervena, zluta, *zelena) = tuple

print(zelena)
```
```
conzole: ["jablko", "meloun"]
```
> Pokud se dáme `*` k proměnné mezi, přiřadí se ji, všechny volné hodnoty od její pozice

```python
tuple = ("jahoda", "banán", "jablko", "meloun")

(cervena, *zluta, zelena) = tuple

print(zluta)
print(zelena)
```
```
conzole: ["banán", "jablko"]
conzole: meloun
```

## Závěr

Hlavní rozdíl mezi tuple a listem je ten, že tuple se "nedají" měnit. Proto fungují jako stabilněší způsob uložení dat se stejně jednoduchým přístupem.

Jak listy tak i tuples mají svá využití, a záleží jen na tom, co v danou chvíli potřebujeme.
