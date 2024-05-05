# Formátování textu

V téhle části si ukážeme další možnosti jak v Pythonu můžeme upravovat a formátovat text.

## Úprava textu

Python má spoustu metod pro úpravu text. Na rozdíl od funkcí jako print() se metody používají tak, že se za proměnou napíše `.` a za ní se připojí metody, kterou chceme použít.
Metodu můžeme používat rouvnou, když chceme vypsat výsledek, mebo jejich výsledek může zapsat do nové proměnné a s tou pracovat pak dál, třeba ji vypsat.
> Metody vrací nové hodnoty, nemění originální text

### Velká písmena

První takouvou metodou je `upper()`, která nám změní veškerá písmena na velká.
```python
a = "malá písmena"
b = a.upper()
print(b)
```
```
conzole: MALÁ PÍSMENA
```

### Malá písmena

Opačnou metodou je metoda `lower()`, která změní všechny písmena na malá písmena.

```python
a = "VelkÁ PíSmeNa"
print(a.lower())
```
```
conzole: velká písmena
```

### Nádrada písmen

Další metodou je metoda `replace()`, kde zadáme co chceme nahradi čím, a ona nám to nahradí. 

```python
a = "test nahrazení"
print(a.replace("e","o"))
```
```
conzole: tost nahrazoní
```
> První je co chceme nahradit a druhý je za co, může se jednat i o delší část než jen jedno písmeno

Tahle metoda se dá použít i pro odstranění části text, kde část nahradíme prázdnem

```python
a = "odstraň tuhle část"
b = a.replace("tuhle ","")
print(b)
```
```
conzole: odstraň část
```

### Rozdělení textu

Pokud chceme rozdělit text na části použijeme metodu `split()`, do které vložíme znak na kterém chemem text rozdělit a vrátí nám list části.(co je to list si řekneme v dalším modulu)

```python
a = "rozděl, text"
b = a.split(",")
print(b)
```
```
conzole: ["rozděl"," text"]
```
> Hranaté závorky označují, že se jedná o list

### vkládání proměný do textu

Minule jsme si ukázali, jak můžeme spojovat text s dalšími proměnými, teď si ukážeme metodu, která nám to zjednodušuje a umožňuje nám vkládat proměnné přímo do textu.
Jedná se o metodu `format()`, ale používá se trochu jinak, než předchozí metody. Pokud ji chceme použít, tak před text dáme písmeno `f`. Pokud pak do textu chceme vložit proměné, napíšeme jejich jméno do složených závorek `{}`.

```python
cena = 68
text = f"Maso stojí {cena}Kč za kg."
print(text)
```
```
conzole: Maso stojí 68Kč za kg.
```

Nebo do závorek můžeme vložit i přímo výpočty:
```python
cena = 25
text = f"Maso stojí {cena*3}Kč za kg."
print(text)
```
```
conzole: Maso stojí 75Kč za kg.
```

## Další zajímavé metody
|metoda|co dělá|příklad|
|---|---|---|
|count()|Spočítá, kolikrát se zadaná část vyskatovala v text|count("a"), kolikrát se v text vyskytlo písmeno a
|find()|Hledá v text zadanou část vrátí na jaké pozici ji to našlo|find("jak"), vrátí číslo pozice, kde začne slovo jak|
|swapcase()|Z velkých písmen udělá malé a z malých velká|žádný argumenty nepoužívá|
|title()|První písmeno každé slova se změní na velké||
|isalpha()|Vrátí pravda, pokud jsou v textu pouze písmena||
