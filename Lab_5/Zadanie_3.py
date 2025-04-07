class Kolejka:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Kolejka jest pusta"
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def show_queue(self):
        return self.queue

# Program główny
kolejka = Kolejka()

while True:
    menu = """\nWybierz działanie:
1. Zarejestruj pacjenta
2. Wywołaj pacjenta do gabinetu
3. Pokaż aktualną kolejkę
4. Zakończ działanie programu\n"""
    choice = input(menu)

    if choice == "1":
        pacjent = input("Podaj imię pacjenta: ")
        kolejka.enqueue(pacjent)
    elif choice == "2":
        print("Wywołano:", kolejka.dequeue())
    elif choice == "3":
        print("Aktualna kolejka:", kolejka.show_queue())
    elif choice == "4":
        break
    else:
        print("Nieprawidłowy wybór.")
