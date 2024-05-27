# Slovníky

## Základní informace

Slovníky slouží k ukládá párů hodnot do jedné proměnné a poznáme je podle toho, že jsou ohraničeny složenými závorkami `{}` a obsahují páry ve formátu `klíč:hodnota`.

Slovník se vytváří zápisem
```python
slovnik = {"jablko":"apple","banan":"banana"}
```

a hodnoty v něm hledáme pomocí klíče následovně:
```python
slovnik["jablko"]
```
```výsledek
Console: "apple"
```

Jelikož slovník jako hodnotu udrží jakýkoliv datový typ, můžou slovníky být i komplikovanější:
```python
slovnik = {"A":321,"B":[11,22,33],"C":["ahoj","cau","nazdar"]}
```

Ale i s takovým slovníkem pracujeme pořád stejně:
```python
slovnik["C"]
```
```výsledek
Console: ["ahoj","cau","nazdar"]
```
a
```python
slovnik["C"][1]
```
```výsledek
Console: ["cau"]
```

## Změny ve slovníku


Měnění hodnot je také docela jednoduché:
```python
slovnik["A"]
```
```výsledek
Console: 321
```
a
```python
slovnik["A"] = slovnik["A"] - 1
slovnik["A"]
```
```výsledek
Console: 320
```

Stejným způsobem můžeme i přidat nové páry klíčů a hodnot:
```python
slovnik["D"] = "uz_fakt_posledni_hodnota"
slovnik
```
```výsledek
Console: {"A":321,"B":[11,22,33],"C":["ahoj","cau","nazdar"], "D":"uz_fakt_posledni_hodnota"}
```

Dokonce se do slovníku dá nacpat i další celý slovník:
```python
slovnik = {"klíč1":{"klíč11":{"klíč111":"hodnota"}}}
slovnik["klíč1"]["klíč11"]["klíč111"]
```
```výsledek
Console: "hodnota"
```


## Užitečné metody


Pokud máme slovník slovnik
```python
slovnik = {"klíč1":1,"klíč2":2,"klíč3":3}
```
často se nám bude hodit projít seznamem (listem) klíčů,

```python
slovnik.keys()
```
```výsledek
Console: dict_keys(["klíč1", "klíč2", "klíč3"])
```

hodnot

```python
slovnik.keys()
```
```výsledek
Console: dict_values([1, 2, 3])
```

anebo celých párů ve formátu tuplů

```python
slovnik.items()
```
```výsledek
Console: dict_items([("klíč1", 1), ("klíč2", 2), ("klíč3", 3)])
```

