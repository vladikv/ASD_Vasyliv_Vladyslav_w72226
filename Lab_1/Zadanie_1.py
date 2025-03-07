import math


def rozwiaz_rownanie_kwadratowe(a, b, c):
    # Sprawdzanie, czy współczynnik a jest różny od zera
    if a == 0:
        return "Współczynnik a nie może być zerem w równaniu kwadratowym!"

    # Obliczenie delty
    delta = b ** 2 - 4 * a * c

    # Przypadek 1: Dwa różne pierwiastki rzeczywiste (delta > 0)
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Dwa pierwiastki rzeczywiste: x1 = {x1}, x2 = {x2}"

    # Przypadek 2: Jeden pierwiastek podwójny (delta = 0)
    elif delta == 0:
        x = -b / (2 * a)
        return f"Jeden pierwiastek podwójny: x = {x}"

    # Przypadek 3: Brak pierwiastków rzeczywistych (delta < 0)
    else:
        return "Brak pierwiastków rzeczywistych."


a = float(input("Podaj współczynnik a: "))
b = float(input("Podaj współczynnik b: "))
c = float(input("Podaj współczynnik c: "))

wynik = rozwiaz_rownanie_kwadratowe(a, b, c)
print(wynik)
