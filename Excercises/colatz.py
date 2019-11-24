print("Podaj liczbę:")
number = int(input())


def colatz(number):
    # liczba = int(input())
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


print(colatz(number))

import copy
lista1 = ["a", "b", "c"]
lista2 = copy.copy(lista1)
