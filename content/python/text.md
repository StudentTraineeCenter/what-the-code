# Práce s textem - string

V téhle části si ukážeme jek se v Pythonu pracuje s textem.

## String

Text se v pythonu označuje jako string a poznáme ho tím, že je uzavřen do uvozovek: `"text"` nebo `'text'`
Na tom, který typ uvozovek použijeme nezáleží.

Pokud pak chceme vypsat náš text, tak opět použijeme funkci print()
```python
print("Ahoj")
```
nebo
```python
text = "ahoj"
print(text)
```

## Možné operace s textem

### Části textu

Když máme text, můžeme chtít použít jen jeho část:
Pro jeden charakter z textu:
```python
text = "Nazdar světe"
print(text[2])
```
```python
console: z
```
> Do hranatých závorek dáme pozici nešeho znaku. (počítá se od začítku od 0)

Pokud chceme část textu, použijeme index 1. a posledního znaku, kterých chceme, odělených pomocí `:`:
```python
text = "Nazdar světe"
print(text[2:6])
```
```python
console: zdar
```
> Poslední znak neni součástí výpisu


Pokud chceme výpis od záčátku někam, nebo od místa do konce, druhé číslo vynecháme:
Od začátku až po r:
```python
text = "Nazdar světe"
print(text[:6])
```
```python
console: Nazdar
```
> Poslední zank není opět započítán


Od mezery do konce:
```python
text = "Nazdar světe"
print(text[6:])
```
```python
console: světe
```


### Spojování textu

Pokud máme více proměných s textem, můžeme je chtít spojit. To se stejně jako u čísel dělá mocí součtu:
Při spojování k nim můžeme vkládat další text:

```python
text1 = "Nazdar"
text2 = "světe"
text = text1 + " " + text2
print(text)
```
```python
console: Nazdar světe
```


Do textu můžeme vkládat i čísla z jiných porměných, ale při vkládání musíme upřesnit že se mají vložit jako text
toho docílíme tím, že je dáme do závorek a před nanpíšeme str(zktratka pro string):
```python
vek = 15
text = "Je mi "
print(text + str(vek) + " let.")
```
```python
console: Je mi 15 let.
```

### Speciální znaky

Při práci s textem můžeme využívat speciálních znaků pro jeho úpravu:
|zank|k čemu|
|---|---|
|`\"`|pokud chceme použít uvozovky uvnitř text, jinak jsou braný jako konec textu|
|`\\`|zpětné lomítko normálně označuje speciální znak, pokud chceme \ jako takové musíme použít dvě|
|`\n`|funguje jako enter a na dané pozici zalomí text na nový řádek|
|`\t`|na daném místě udělá mezeru jako při použití Tab klávesy|

```python
text = "Nazdar\n\t\"světe\""
print(text)
```
```python
console: Nazdar
           "světe"
```

## Shrnutí

Python dokáže s textem dělat hodně operací a to, co jsme si zde ukázali je pouze špička ledovce.

Pro více možností a funkcí, které usnadňují práci s textem se podívejte na modul text2.
