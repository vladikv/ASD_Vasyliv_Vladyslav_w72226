def selection_sort(arr):
    comparisons = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"Po iteracji {i+1}: {arr}")
    return arr, comparisons

wagi_paczek = [18, 5, 12, 3, 9]
posortowane_paczki, liczba_porowan = selection_sort(wagi_paczek)

print("\nPosortowane paczki:", posortowane_paczki)
print("Liczba porównań:", liczba_porowan)
