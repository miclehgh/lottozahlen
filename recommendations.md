# Ideen zum Verbessern

Arbeite die Aufgaben der Reihe nach durch. Starte das Programm nach jeder Änderung und prüfe, ob es sich noch gleich verhält.

## 1. Grenzen als Konstanten speichern

`MAX_ZAHLEN` gibt es schon. Ergänze Konstanten für die kleinste und größte erlaubte Zahl:

```python
MIN_ZAHL = 1
MAX_ZAHL = 49
```

Ersetze dann die festen Zahlen `1` und `49` in der Eingabeprüfung und beim Ziehen durch diese Namen. So musst du die Regeln später nur an einer Stelle ändern.

**Prüfen:** Das Programm soll weiterhin nur Zahlen von 1 bis 49 annehmen.

## 2. Aufgaben in Funktionen aufteilen

Eine Funktion ist ein benannter Abschnitt Code, den du aufrufen kannst. Verschiebe jeweils einen zusammengehörenden Teil des Programms in eine Funktion:

- `tipps_eingeben()` fragt die sechs Zahlen ab und gibt die Tipp-Liste zurück.
- `ziehung_erstellen()` erzeugt und gibt sechs Zufallszahlen zurück.
- `richtige_zahlen_finden(tipps, ziehung)` findet und gibt die richtigen Tipps zurück.

Beginne mit nur einem Teil. Schreibe `def funktionsname():` darüber und rücke den zugehörigen Code ein. Verwende `return liste`, wenn die Funktion eine Liste zurückgeben soll. Rufe die Funktion anschließend auf und speichere das Ergebnis, zum Beispiel `tipps = tipps_eingeben()`.

**Prüfen:** Nach dem Aufteilen soll das Programm dieselben Listen und Ergebnisse ausgeben wie vorher.

## 3. Zufallszahlen einfacher ziehen

Aktuell zieht das Programm eine Zahl nach der anderen und prüft, ob sie schon gezogen wurde. `random.sample()` kann sechs verschiedene Zahlen direkt auswählen. Ersetze den Abschnitt, der `zufallszahlen` füllt, durch:

```python
zufallszahlen = random.sample(range(1, MAX_ZAHL + 1), MAX_ZAHLEN)
```

`range` beginnt bei 1. Das Ende ist exklusiv, darum steht dort `MAX_ZAHL + 1`. `sample` wählt keine Zahl doppelt.

**Prüfen:** Starte das Programm mehrmals. Die Ziehung muss jedes Mal sechs verschiedene Zahlen zwischen 1 und 49 enthalten.