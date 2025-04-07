import heapq

class KolejkaZadan:
    def __init__(self):
        self.heap = []

    def dodaj_zadanie(self, nazwa, priorytet):
        heapq.heappush(self.heap, (priorytet, nazwa))

    def obsluz_zadanie(self):
        if self.heap:
            priorytet, nazwa = heapq.heappop(self.heap)
            print(f"Obsłużono zadanie: {nazwa} (priorytet: {priorytet})")
        else:
            print("Brak zadań do obsługi.")

    def pokaz_kolejke(self):
        print("Aktualna kolejka zadań:")
        for p, n in sorted(self.heap):
            print(f"{n} (priorytet: {p})")

# Program główny
zadania = KolejkaZadan()

while True:
    menu = """\nWybierz działanie:
1. Dodaj zadanie z priorytetem
2. Obsłuż zadanie o najwyższym priorytecie
3. Pokaż kolejkę zadań
4. Zakończ działanie programu\n"""
    wybor = input(menu)

    if wybor == "1":
        nazwa = input("Podaj nazwę zadania: ")
        priorytet = int(input("Podaj priorytet (niższa liczba = wyższy priorytet): "))
        zadania.dodaj_zadanie(nazwa, priorytet)
    elif wybor == "2":
        zadania.obsluz_zadanie()
    elif wybor == "3":
        zadania.pokaz_kolejke()
    elif wybor == "4":
        break
    else:
        print("Nieprawidłowy wybór.")
