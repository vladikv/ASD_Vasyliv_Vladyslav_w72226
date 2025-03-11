def znajdz_min_max(macierz):

    min_wartosc = float('inf')
    max_wartosc = float('-inf')
    min_indeks = (-1, -1)
    max_indeks = (-1, -1)


    for i in range(len(macierz)):
        for j in range(len(macierz[i])):

            if macierz[i][j] < min_wartosc:
                min_wartosc = macierz[i][j]
                min_indeks = (i, j)

            if macierz[i][j] > max_wartosc:
                max_wartosc = macierz[i][j]
                max_indeks = (i, j)


    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if (i, j) == min_indeks:
                macierz[i][j] = 'MIN'
            elif (i, j) == max_indeks:
                macierz[i][j] = 'MAX'


    for wiersz in macierz:
        print(wiersz)



macierz = [
    [5, 2, 9, 8],
    [1, 7, 3, 4],
    [6, 0, 2, 5]
]

znajdz_min_max(macierz)
