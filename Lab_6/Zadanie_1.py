def bubble_sort(arr):
     n = len(arr)
     for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
     return arr


n = int(input("Podaj liczbę graczy: "))
wyniki = []

for i in range(n):
    wynik = int(input(f"Podaj wynik gracza {i+1}: "))
    wyniki.append(wynik)


wyniki_posortowane = bubble_sort(wyniki)


print("Posortowane wyniki:", wyniki_posortowane)
print("Najniższy wynik:", min(wyniki_posortowane))
print("Najwyższy wynik:", max(wyniki_posortowane))