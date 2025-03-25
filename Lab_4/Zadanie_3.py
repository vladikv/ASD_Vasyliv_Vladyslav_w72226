def undo():

    stos = []

    while True:
        polecenie = input("Wprowadź tekst (lub 'Undo' aby cofnąć ostatnią operację, 'exit' aby zakończyć): ")

        if polecenie == 'exit':
            print("Program zakończony.")
            break
        elif polecenie.lower() == 'undo':
            if stos:
                ostatni_tekst = stos.pop()
                print(f"Ostatnia operacja została cofnięta: {ostatni_tekst}")
            else:
                print("Brak operacji do cofnięcia.")
        else:
            stos.append(polecenie)
            print(f"Tekst dodany: {polecenie}")


undo()
