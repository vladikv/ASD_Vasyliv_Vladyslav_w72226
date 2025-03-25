def wynik(i):
    if i < 5:
        return 2
    elif i % 2 == 0:
        return wynik(i - 4) + wynik(i - 2) + 2
    else:
        return wynik(i - 2) % 9

for i in range(1, 16):
    print(f"i={i}, wynik(i)={wynik(i)}")