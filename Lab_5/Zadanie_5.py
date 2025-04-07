from collections import deque

class Klient:
    def __init__(self, imie, czas_obslugi):
        self.imie = imie
        self.czas_obslugi = czas_obslugi

class KolejkaSklepowa:
    def __init__(self):
        self.kolejka = deque()

    def dodaj_klienta(self, imie, czas_obslugi):
        klient = Klient(imie, czas_obslugi)
        self.kolejka.append(klient)
        print(f"Dodano klienta {imie} z czasem obsługi {czas_obslugi} minut.")

    def obsluz_klienta(self):
        if not self.kolejka:
            print("Brak klientów w kolejce.")
            return
        klient = self.kolejka.popleft()
        print(f"Obsłużono klienta {klient.imie}. Czas obsługi: {klient.czas_obslugi} minut.")

    def wyswietl_kolejke(self):
        if not self.kolejka:
            print("Kolejka jest pusta.")
            return

        print("Aktualna kolejka z czasami oczekiwania:")
        suma_czasu = 0
        for klient in self.kolejka:
            print(f"{klient.imie} - czas oczekiwania: {suma_czasu} minut")
            suma_czasu += klient.czas_obslugi


kolejka = KolejkaSklepowa()

while True:
    menu = """\nWybierz opcję:
1. Dodaj klienta do kolejki
2. Obsłuż klienta
3. Wyświetl kolejkę z czasami oczekiwania
4. Zakończ program\n"""
    wybor = input(menu)

    if wybor == "1":
        imie = input("Podaj imię klienta: ")
        try:
            czas = int(input("Podaj szacowany czas obsługi (w minutach): "))
            kolejka.dodaj_klienta(imie, czas)
        except ValueError:
            print("Nieprawidłowy czas – podaj liczbę całkowitą.")
    elif wybor == "2":
        kolejka.obsluz_klienta()
    elif wybor == "3":
        kolejka.wyswietl_kolejke()
    elif wybor == "4":
        print("Zamykanie programu...")
        break
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
