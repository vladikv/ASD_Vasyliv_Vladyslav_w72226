krawedzie = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E')]


sasiadztwo = {}
for u, v in krawedzie:
    sasiadztwo.setdefault(u, []).append(v)
    sasiadztwo.setdefault(v, []).append(u)

print("Lista sąsiedztwa:")
for w in sasiadztwo:
    print(f"{w}: {sasiadztwo[w]}")


wierzcholki = sorted(set(sum(krawedzie, ())))
indeksy = {w: i for i, w in enumerate(wierzcholki)}
n = len(wierzcholki)

macierz = [[0]*n for _ in range(n)]
for u, v in krawedzie:
    i, j = indeksy[u], indeksy[v]
    macierz[i][j] = 1
    macierz[j][i] = 1

print("\nMacierz sąsiedztwa:")
print("  " + " ".join(wierzcholki))
for i, w in enumerate(wierzcholki):
    print(w, " ".join(str(x) for x in macierz[i]))
