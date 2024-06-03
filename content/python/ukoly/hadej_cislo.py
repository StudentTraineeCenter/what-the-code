import random # připojení knihovny pro generování náhodného čísla

tajne = random.randint(1,100) # vygenerování náhodné čísla od 1 do 100

pokusy = 0

while True:
    cislo = int(input("Jaké číslo si myslíš:")) # hráč typne číslo
    if cislo < 1 or cislo > 100: # pokud je mimo rozsah, tak typne znovu
        print("Číslo neni v rozsahu od 1 do 100!")
        continue

    if cislo < tajne: # řekne jak je jeho číslo oproti hádanému
        print("Hádané číslo je větší!")
    elif cislo > tajne:
        print("Hádané číslo je menší!")
    else:
        print("Gratuluji, uhádl jsi číslo:" + str(tajne))
        print("Trvalo ti to " + str(pokusy) + "pokusů.")
        break
    pokusy += 1