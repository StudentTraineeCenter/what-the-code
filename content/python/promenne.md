# Data v pythonu

## Typy dat

V pythonu rozlišujeme různé datové typy a podle toho s nimi dále pracujeme.

|datový typ|co do něj uložit|
|---|---|
|text (string)|Datový typ pro ukládání textu|
|čísla (int)|Datový typ pro ukládání celých čísel|
|čísla (fload)|Datový typ pro ukládání čísel s desetinou čárkou|
|Pravda/Nepravda(Boolean)|Datový typ pro ukládání Pravda/Nepravda rozhodnutí|
|list|Datový typ pro ukládání více hodnot do jedné proměnné|

Datových typů v pythonu je víc, ale o nich si povíme až v dalších modulech.

## Proměnné

Pokud chceme v pythonu a v programování obecně pracovat s daty, tak je musíme uložit do proměnných.
Každý proměnná musí mít svůj unikátní název.
Ukládání do proměnných funguje tak, že napíšeme její název a čemu se rovná.

```python
test = "ahoj"
známka = 2
zpráva = "ET volá domů."
```

Pokud chceme vatvořit několik proměnný se stejnou hodnotou najednou můžeme je nechat se rovnat sami sobě.

```python
cislo1 = cislo2 = 3
```

Nebo můžme spojit přiřazování hodnot proměnných do jednoho řádku.

```
a,b,c = "a","b","c"
```

> kde `a` se bude rovnat "a", `b` rovnat "b" a `c` rovnat "c"

Pokud s proměnnýma budeme pracovat, musíme je nejprve vytvořit, python provádí kód postupně po řádcích, tudíž pokud neni proměnná nejprve vytvořena, do té doby nebude znát.

## Vypsání do příkazového řádku

Pokud chceme, aby nám program něco vypisoval, použijeme funkci `print()`
Do závorka pak dáme to, co chceme vypsat.
Může to být ručně nastavená hodnota, nebo aktuální obsah proměnné.

```python
text = "ahoj"

print(1)
print(text)
print("test")
```
```
conzole: 1
ahoj
test
```

Pokud chceme vypsat více proměnných najednou, oddělíme je čárkou.

```python
text = "ahoj,"
text2 = "já jsem Karel"

print(text, text2)
```
```
conzole: ahoj, já jsem Karel
```

> Při výpisu pak budou odděleny mezerou

## Data od uživatele

Pokud chceme, aby nám uživatel zadával nějaké vstupy, použijeme funkci `input()`
Do závorek pak můžeme napsat text, který se uživateli vypíše před zadáním.
Děláme to tak, že nějakou proměnnou nastavíme že se bude rovnat tomu, co uživatel zadá.

```python
text = input("Zadej svoje jméno: ")
print("Zadal jsi ", text)
```
```
conzole: Zadej svoje jméno: Karel
Zadal jsi Karel
```

> Pozor, uživatelský vstup je většinou braný jako text, tudíž někdy je třeba ho upravit na jiný typ proměnné.

## komnetáře

Pokud chceme do našeho kódu přidat komentář, kterým třeba popíše danou část kódu, ale nechceme aby překážel, dáme před něj `#`
Vše co je z # je na daném řádku ingnorováno a souží to čistě jako popisek.

```python
# vytvoření proměnných
a = "a"
b = 1

# vstup od uživatele
c = input("Zadej svůj věk: ")

# vypsání věku a proměnných
print("Tvůj věk je", c)
```
