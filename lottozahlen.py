import random

MAX_ZAHLEN: int = 6
print("Geben Sie 6 Zahlen zwischen 1 und 49 ein.")

getippte_zahlen: list[int] = []
while len(getippte_zahlen) < MAX_ZAHLEN:
    try:
        zahl: int = int(input(f"Ihre {len(getippte_zahlen) + 1}. Zahl bitte: "))

        if zahl < 1 or zahl > 49:
            print("Diese Zahl liegt außerhalb des erlaubten Bereichs.")
        elif zahl in getippte_zahlen:
            print("Diese Zahl haben Sie bereits getippt.")
        else:
            getippte_zahlen.append(zahl)
    except ValueError:
        print("Geben Sie bitte eine Zahl ein.")

print(getippte_zahlen)

zufallszahlen: list[int] = []
while len(zufallszahlen) < MAX_ZAHLEN:
    zufallszahl: int = random.randint(1, 49)
    if zufallszahl not in zufallszahlen:
        zufallszahlen.append(zufallszahl)

print(zufallszahlen)

richtige: list[int] = []
for zahl in getippte_zahlen:
    if zahl in zufallszahlen:
        richtige.append(zahl)

print(f"Sie haben {len(richtige)} Richtige.")
print(f"Diese Zahlen haben Sie richtig geraten: {richtige}")
