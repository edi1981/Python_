import random
number = random.randint(1, 20)
print(number)

print("Podaj liczbę z zakresu 1 - 20: ")
g_number = int(input())
if g_number == number:
    print("OK")
else:
    while g_number != number:

        if g_number < number:
            print("mala:")
            print("Podaj liczbę z zakresu 1 - 20: ")
            g_number = int(input())
        elif g_number > number:
            print("duza:")
            print("Podaj liczbę z zakresu 1 - 20: ")
            g_number = int(input())
        if g_number == number:
            print("Tak to ta liczba:", g_number)








