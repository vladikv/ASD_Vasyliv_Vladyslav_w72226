def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


        steps.append((i, key, j, f"A[{j}] > element", arr[:]))
    return arr, steps

oceny = [3, 5, 2, 6, 4, 1]
posortowane, kroki = insertion_sort(oceny)

# Wyświetlenie wyników
print("Posortowane oceny:", posortowane)
print("\nTabela kroków:")
print("Krok i | Wstawiany element | j | Porównanie A[j] > element | Stan tablicy po wstawieniu")
for krok in kroki:
    print(f"{krok[0]} | {krok[1]} | {krok[2]} | {krok[3]} | {krok[4]}")
