def sprawdz_nawiasy():
    wyrazenie = input("Wprowadź wyrażenie z nawiasami: ")

    stos = []

    for znak in wyrazenie:
        if znak == '(':
            stos.append(znak)
        elif znak == ')':
            if stos:
                stos.pop()
            else:
                print("Nawiasy są nieprawidłowo zagnieżdżone.")
                return


    if not stos:
        print("Nawiasy są prawidłowo zagnieżdżone.")
    else:
        print("Nawiasy są nieprawidłowo zagnieżdżone.")


sprawdz_nawiasy()
