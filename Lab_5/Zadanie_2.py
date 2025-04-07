from collections import deque


def get_n_elements(queue, n):
    if not queue:
        return "Kolejka jest pusta"
    return list(queue)[:n]

# Przykład użycia
q = deque(["a", "b", "c"])
print(get_n_elements(q, 5))
