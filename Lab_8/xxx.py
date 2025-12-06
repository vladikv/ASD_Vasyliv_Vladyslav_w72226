def wyszukiwanie_liniowe(lista, szukana_wartosc):
    for indeks in range(len(lista)):
        # Sprawdzamy czy aktualny element jest równy szukanej wartości
        if lista[indeks] == szukana_wartosc:
            # Jeśli tak zwracamy jego indeks
            return indeks

    return "Element nie znajduje się w liście."


lista_liczb = [4, 7, 2, 9, 5, 1]
wartosc_do_znalezienia = 9

wynik = wyszukiwanie_liniowe(lista_liczb, wartosc_do_znalezienia)
print("Wynik wyszukiwania:", wynik)
