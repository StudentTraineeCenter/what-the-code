# Kontrola palindromu

## Zadání

Program přijme od uživatele slovo a vrátí, zda se jedná o palindrom či nikoliv.
Palindrom je slovo, které se čte stejně od zadu jako ze předu.

Příklad palindromu: oko, madam, radar, nepotopen...

::show
## Řešení

```python
slovo = input("Zadej slovo:")

for x in range(len(slovo)//2): # zjistí celočíselnou půlku délky slova
    if slovo[x] != slovo[-(x+1)]: # pokud dvě se dvě opačná písmena nerovnají
        print("Slovo neni palindrom!")
        break
else: # pokud se všechny opačná písmena rovnají a dojde k dokončení cyklu
    print("Slovo je palindrom!")
```

zkratka:
v pythonu můžeme otočit pořadí v seznamu pomocí [::-1] pak místo slova ahoj bude joha
zároveň v pythonu můžeme porovnávat dva texty, zda jsou shodné nebo ne

```python
slovo = input("Zadej slovo:")
if slovo == slovo[::-1]:
   print("slovo je palindrom!")
else:
   print("Slovo neni palindrom!")
```
::