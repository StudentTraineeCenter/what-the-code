# Podmínky
V Pythonu používáme podmíněné příkazy pro řízení částí programu na základě určitých podmínek. Programu zadáme určitou podmínku. Pokud je podmínka splněna, spustí se příkaz uvnitř podmínky, pokud není splněna příkaz uvnitř je ignorován a program pokračuje dále.

## použití

Používáme výraz `if`, příkat uvnitř těla vždy oddělujeme tabulátorem, v momentě kdy nezačneme tabulátorem, udáváme tím konec podmínky.

```python
if 15 > 0:
    # provede se, pokud je podminka pravdiva
    print("podmínka je pravdivá")
print("Konec programu")
```
>Jako podmínku jsme udali, že číslo 15 musí být větší než číslo 0. To pravda je, program tedy vypíše text "Podmínka je pravdivá". Dále vystoupí z podmínky a pokračuje dále v programu.

Do podmínek můžeme zapojit i proměnné:

```python
a = int(input("Zadej celé číslo: "))
if a == 0:
    print("a je rovno 0")
print("Konec programu")
```

> Nyní žádáme uživatele o vložení celého čísla, které bude reprezentovat hodnotu proměnné "a". Pokud se rovná číslu 0, podmínka je splněna

### porovnávací operátory

Pro zapsání výrazu podmínky můžeme používat několik operátorů sloužící k porovnání hodnot:

|Význam|Operátor|
|------|------|
|Rovná se|==|
|Nerovná se|!=|
|Menší než|<|
|Menší nebo rovno|<=|
|Větší než|>|
|Větší nebo rovno|>=|



### if..else podmínka

K samotné `if` podmínce lze přidat dodatek `else`. Výraz `else` se spustí pokud vyjde původní podmínka `if` jako `nepravda`

```python
x = int(input("x + 10 = 15; Doplň x aby byla rovnice pravdivá:"))
if x + 10 == 15:
    print('Rovnice je pravdivá')
else:
    print('Rovnice není pravdivá')
print("Konec programu")
```
>Po spuštění programu jsme vyzvání k vyřešení rovnice. Pokud doplníme číslo 5, podmínka bude pravdivá a spustí se příkaz uvnitř těla `if` podmínky.
>Pokud zadáme jakékoliv jiné číslo, například -5, podmínka se nesplní, příkaz v tělě `if` podmínky bude přeskočen a spustí se příkaz v tělě `else`

>V obou případech následuje vypsání "Konec programu", to se nachází mimo podmínku a spustí se bezprostředně po ukončení podmínky. 

### if..elif..else podmínka

Pokud potřebujeme více než jednu alternativu pro podmínku `if`, použíjeme výraz `if` - `elif` - `else`. "elif" jako "else if"

```python
x = 0
if x > 0:
    print("Kladné číslo")
elif x < 0:
    print("Záporné číslo")
else:
    print("Nula")
print("Konec programu")
```
```
výstup:
Nula
Konec programu
```

>Číslo pro podmínku jsme udali 0. Spustí se začátek podmínky `if`, kde se porovná naše číslo ve vztahu `0 > 0`. To pravda není, příkaz v tělě `if` je ignorován a program se posouvá na druhou podmínku `elif`, zde podmínka také není splněna.
>Nebyla tedy splněna ani jedna podmínka a tak program vypíše příkaz těla `else`

### Vnořování if podmínek

Kromě vytváření samotných `if` podmínek můžeme i jednotlivé podmínky vnořovat do sebe.

```python
x = int(input("Zadej kladné číslo:"))
if x > 0:
    y = int(input("Zadej číslo které není kladné ani záporné:"))
    if y == 0:
        print("Správně")
    else:
        print("Zkus to znovu!")
else:
    print("To není kladné číslo")
print("Konec programu")
```

>Uživatel je vyzván zadat kladné číslo, pokud tak neučiní, je přesunut příkaz těla `else` na konci kódu. Pokud ano, kód pokračuje uvnitř první `if` podmínky. Zde je opět výzva zadat číslo. Začíná zcela nová podmínka, pokud je splněna vypíše se "správně", pokud ne přesune se program na vnořenou `else` větev, vypíše "Zkus to znovu!" a skočí za celou `if` podmínku, tedy vypíše "Konec programu"

příklad možných výstupů
```
výstup:
Zadej kladné číslo:654
Zadej číslo které není kladné ani záporné:4
Zkus to znovu!
Konec programu
```
```
výstup:
Zadej kladné číslo:-5
To není kladné číslo
Konec programu
```
```
výstup:
Zadej kladné číslo:10
Zadej číslo které není kladné ani záporné:0
Správně
Konec programu
```

## úkoly na procvičení

Naprogramuj kód, který vyžádá uživatele o vyřešení několika matematických operací. Pokud některou z nich nezodpoví správně, program skončí. NÁPAD
