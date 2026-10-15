import random

zufallszahlen: list[int] = []
getippte_zahlen: list[int] = []
richtige: list[int] = []

# Benutzereingabe: 6 Lottozahlen
fertig_getippt: bool = False
print("Geben Sie 6 Zahlen zwischen 1 und 49 ein.")
eingabe_counter: int = 1
while not fertig_getippt:
    try:
        zahl: int = int(input(f"Ihre {eingabe_counter}. Zahl bitte: "))
        if zahl not in getippte_zahlen and 0 < zahl < 50:
            getippte_zahlen.append(zahl)
            eingabe_counter += 1
        else:
            if zahl in getippte_zahlen:
                print("Diese Zahl haben Sie bereits getippt.")
            if zahl < 1 or zahl > 49:
                print("Diese Zahl liegt außerhalb des erlaubten Bereichs.")
    except ValueError:
        print("Geben Sie bitte eine Zahl ein.")
    if len(getippte_zahlen) == 6:
        fertig_getippt = True
print(getippte_zahlen)

# Zufallszahlen erzeugen
fertig_zufallszahlen_erzeugen: bool = False
while not fertig_zufallszahlen_erzeugen:
    zufallszahl: int = random.randint(1, 49)
    if zufallszahl not in zufallszahlen:
        zufallszahlen.append(zufallszahl)
    if len(zufallszahlen) == 6:
        fertig_zufallszahlen_erzeugen = True
print(zufallszahlen)

# Anzahl richtiger Tipps testen.
# Richtige Tipps in eine neue Liste schreiben.
counter: int = 0
while counter < 6:
    if getippte_zahlen[counter] in zufallszahlen:
        richtige.append(getippte_zahlen[counter])
    counter += 1
print(f"Sie haben {richtige} Richtige.")
print(f"Sie haben folgende Zahl(en) richtig geraten: {richtige}")
