graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}


def wypisz_sasiadow(graf, wierzcholek):
    return graf.get(wierzcholek, [])

print("Sąsiedzi wierzchołka C:", wypisz_sasiadow(graph, 'C'))
