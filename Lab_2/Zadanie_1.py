def druga_najwieksza(lista):

    unikalne_liczby = set(lista)


    if len(unikalne_liczby) < 2:
        return None


    posortowane_liczby = sorted(unikalne_liczby, reverse=True)


    return posortowane_liczby[1]


print(druga_najwieksza([3, 1, 4, 1, 5, 9, 2, 6]))
print(druga_najwieksza([10, 20, 20, 10]))
print(druga_najwieksza([1, 1, 1, 1]))
print(druga_najwieksza([5, 6, 7]))
