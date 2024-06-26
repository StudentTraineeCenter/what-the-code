# Listy = uložení více hodnot do jedné proměnné

## Základní informace

Listy slouží k ukládá více hodnot do jedné promměné.
Listy poznáme podle toho, že jsou ohraničeny hranatými závorkami `[]`.

Vytvoření listu:
```python
list = [1, 2, 3]
print(list)
```
```
conzole: [1, 2, 3]
```
> Jednotlivé hodnoty jsou odděleny `,`, pokud se jedná o text, musí být zapsán v uvozovkách.

Listy jsou **řazený**, neboli na **pořadí záleží**, a v jakém pořadí hodnoty zadáme, v takovém zůstanou.

Tudíž pokud přidáme novou hodnotu, tak se přiřadí na konec. Pořadí je pak **určeno indexem**, který začíná od 0.

Zároveň listy **povolují duplikáty**, takže každá hodnota se tam může vyskytovat kolikrát chceme.

Listy **nejsou definitivní**, takže je můžeme upravovat, přidávat a ubírat hodnoty.

Nakonec jeden list může obsahovat více datových typů najednou.

```python
list = [1, "test", True, 2, 2, "konec"]
```

Pokud potřebujeme zjisit délku našeho listu můžeme použít funkci `len()`:

```python
list = [1, "test", True, 2, 2, "konec"]
print(len(list))
```
```
conzole: 6
```
> Stejná funkce funguje i pro string.

## Přístup k hodnotám a práce s nimi

Pro přístup k hodnotě zadáme do hranatých závorek pozici hodnoty/hodnot, které se snažíme získat:

```python
list = [1, "test", True, 2, 2, "konec"]
print(list[1])
```
```
conzole: test
```

Pokud chceme počítat od zadu, použijeme záporné číslo:

```python
list = [1, "test", True, 2, 2, "konec"]
print(list[-2])
```
```
conzole: 2
```

Pro přístup k části listu, stejně jako u textu dáme do hranatých závorek číslo prvního a posledního indexu oddělé `:`

```python
list = [1, "test", True, 2, 2, "konec"]
print(lsit[1:4])
```
```
conzole: ["test", True, 2]
```

### Změna hodnot v listu

Funguje stejně jako přidělení hodnoty k proměnný, ale musíme zadat pozici, na kterou chceme hodnotu zapsat:

```python
list = [1, 2, 3]
list[1] = 5
print(list)
```
```
conzole: [1, 5, 3]
```

Stejným způsobem můžeme nahradit větší množství:

```python
list = [1, 2, 3, 4, 5, 6]
list[1:3] = [7, 8]
print(list)
```
```
conzole: [1, 7, 8, 4, 5, 6]
```

Pokud se tímto způsoběm pokusíme vložit víc/míň hodnot, než je oblast, kterou jsme vybrali, změní se délka listu.

```python
list = [1, 2, 3, 4, 5, 6]
list[1:3] = [7, 8, 9, 10]
print(list)
```
```
conzole: [1, 7, 8, 9, 10, 4, 5, 6]
```

### Přidání dalších hodnot

Pokud hodnoty nechceme přepisovat ale pouze vložit, můžeme použít metodu `insert()`, kde nejprve specifikujeme pozici kam chceme hodnotu vložit a následně co tam chceme vložit:

```python
list = [1, 2, 3, 4, 5, 6]
list.insert(2, "x")
print(list)
```
```
conzole: [1, 2, "x", 3, 4, 5, 6]
```

Nebo pokud nám stačí připojit hodnotu na konec listu máme metodu `append()`, která připojí hodnotu na konec listu:

```python
list = [1, 2, 3, 4, 5, 6]
list.append(7)
print(list)
```
```
conzole: [1, 7, 8, 4, 5, 6, 7]
```

Když chceme spojit dva listy můžeme použít metodu `extend()`

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
```
```
conzole: [1, 2, 3, 4, 5, 6]
```

Máme-li více listů můžeme je spojit pomocí `+` jako u textu:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list = list1 + list2
print(list)
```
```
conzole: [1, 2, 3, 4, 5, 6]
```

### Odstranění hodnot

Když chceme odstranit hodnotu z listu máme pár možností. První z nich je pomocí metody `remove()`, kde zadáme obsah hodnoty, kterou chceme odstranit:
```python
list = ["test", "ahoj", "zmiz", "jablko"]
list.remove("zmiz")
print(list)
```
```
conzole: ["test", "ahoj", "jablko"]
```
> pokud jsou v listu duplicity, odstraní se první výskyt

Další možností odstranění hodnoty je metoda `pop()`, která buď odstraní hodnotu na zadaném indexu, nebo pokud necháme prázdnou odstraní podslední hodnotu v listu:

```python
list = ["test", "ahoj", "zmiz", "jablko"]
list.pop()
print(list)
```
```
conzole: ["test", "ahoj", "zmiz"]
```

Pro odstranění hodnoty na zadaném indexu se dá použít i slovo `del`:

```python
list = ["test", "ahoj", "zmiz", "jablko"]
del list[0]
print(list)
```
```
conzole: ["ahoj", "zmiz", "jablko"]
```

Pomocí del se dá odstranit i celý list:

```python
list = ["test", "ahoj", "zmiz", "jablko"]
del list
```

Poslední metodou je metoda `clear()`, která smaže všechny hodnoty v listu, ale zachová proměnou listu:

```python
list = ["test", "ahoj", "zmiz", "jablko"]
list.clear()
print(list)
```
```
conzole:
```

### vytvoření kopie listu

Pro vytvoření kopie listu nemůžeme použít `list2 = list1`, jelikož pak by se změny v list1 propisovaly do list2.
K vytvoření nezávislé kopie listu můžme použít metodu `copy()`:

```python
list1 = ["test", "ahoj", "zmiz", "jablko"]
list2 = list1.copy()
```

Druhou možností je pomocí metody `list()`:

```python
list1 = ["test", "ahoj", "zmiz", "jablko"]
list2 = list(list1)
```

### Seřazení listu

Když chceme seřadit údaje v listu podle jejich hodnot můžeme použít metodu `sort()`, která je seřadí vzestupně(od A do Z):

```python
list = [4, 10, 9, 32, 7]
list.sort()
print(list)
```
```
conzole: [4, 7, 9, 10, 32]
```
> Pro sestupné řazení: `list.sort(reverse = True)`

## Shrnutí metod

|metoda|popis|
|---|---|
|`append()`|Přidá hodnotu na konec listu|
|`clear()`|Vyprázdní list|
|`copy()`|Vytvoří kopii listu|
|`extend()`|Připojí jiný list na konec aktuální listu|
|`insert()`|Vloží na specifickou pozici|
|`pop()`|Odstraní hodnotu na základě pozice|
|`remove()`|Odstraní hodnotu na základě obsahu|
|`reverse()`|Obrátí pořadí listu|
|`sort()`|Seřadí list vzestupně|

