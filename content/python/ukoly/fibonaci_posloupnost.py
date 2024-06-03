# zeptáme se uživatele na počet čísel
pocet = int(input("Zadej počet čísel:"))

# definujeme první dvě čísla pro počítání
cislo1 = 1
cislo2 = 0

for x in range(pocet):
    print(cislo1) # vypíšeme nejnovější číslo
    novy = cislo1 + cislo2 # zjistíme další číslo
    cislo2 = cislo1 # přepíšeme čísla pro počítání
    cislo1 = novy
