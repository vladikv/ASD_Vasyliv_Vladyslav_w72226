def quick_select(arr, k, krok=1):
    print(f"{'Krok':<5} {'Tablica':<25} {'Pivot':<7} {'Mniejsze':<20} {'Równe':<10} {'Większe':<20} {'k':<5}")

    while True:
        pivot = arr[0]
        mniejsze = [x for x in arr if x < pivot]
        równe = [x for x in arr if x == pivot]
        większe = [x for x in arr if x > pivot]

        print(f"{krok:<5} {str(arr):<25} {pivot:<7} {str(mniejsze):<20} {str(równe):<10} {str(większe):<20} "
              f"{k:<5}")

        if k <= len(mniejsze):
            arr = mniejsze
        elif k <= len(mniejsze) + len(równe):
            return pivot
        else:
            k -= len(mniejsze) + len(równe)
            arr = większe

        krok += 1



tablica = [12, 3, 5, 7, 4, 19, 26]
k = 3

wynik = quick_select(tablica, k)
print(f"\n {k}-ty najmniejszy element to: {wynik}")