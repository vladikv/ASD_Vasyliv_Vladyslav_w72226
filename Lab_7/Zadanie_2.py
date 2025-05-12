def interpolacyjnie_szukaj(lista, szukana):
    start = 0
    end = len(lista) - 1
    krok = 1

    print(f"{'Krok':<5} {'start':<6} {'end':<5} {'mid':<5} {'lista[mid]':<10}")

    while start <= end and lista[start] <= szukana <= lista[end]:

        if lista[end] == lista[start]:
            break

        mid = start + ((szukana - lista[start]) * (end - start)) // (lista[end] - lista[start])

        print(f"{krok:<5} {start:<6} {end:<5} {mid:<5} {lista[mid]:<10}")

        if lista[mid] == szukana:
            print(f"\nZnaleziono wartość {szukana} na indeksie {mid}.")
            return mid
        elif lista[mid] < szukana:
            start = mid + 1
        else:
            end = mid - 1

        krok += 1

    print(f"\nWartość {szukana} nie została znaleziona.")
    return -1



lista = [12, 18, 24, 30, 36, 42, 48, 54, 60]
szukana = 36

interpolacyjnie_szukaj(lista, szukana)