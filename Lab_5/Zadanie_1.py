from collections import deque

queue = deque()

for _ in range(3):
    number = input("Podaj liczbę: ")
    queue.append(number)

print("Elementy kolejki:")
for item in queue:
    print(item)
