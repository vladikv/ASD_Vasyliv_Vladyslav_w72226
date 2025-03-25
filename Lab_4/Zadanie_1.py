def odwroc_ciag():
    liczby = input("Wprowadź ciąg liczb całkowitych oddzielonych spacjami: ").split()

    stos = []

    for liczba in liczby:
        stos.append(int(liczba))

    print("Liczby w odwrotnej kolejności:")
    while stos:
        print(stos.pop())


odwroc_ciag()
