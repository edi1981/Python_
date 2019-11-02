#i = 1
#iMax = 13
#while i <= 13:
#    print((i**2), (i**3), i)
#    i += 1

#start = 0
#end = 16
#x = start
#while x <= end:
#    print("2**",x, 2**x)
#    x += 1


#mamy znaleźć dwie kolejne liczby, gdzie druga liczba jest kwadratem poprzedzającej
numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i = 0
max = len(numbers)-1 #znajdujemy ile elementów ma tablica i pomniejszamy o 1,
                     #bo badamy i porównójemy po 2 liczby na raz i nie moglibyśmy
                     #już porównać ostatniej liczby czyli 11 z kolejną
#print(max)
while i < max:
    print(i, numbers[i], numbers[i+1]) #wyświetlamy po 2 kolejne liczby ze zbioru
    if numbers[i+1] == numbers[i]**2:  #sprawdzamy, które dwie kolejne liczby
                                       # spełniają założony warunek
        print("\tFound:", i, numbers[i], numbers[i+1])
    i += 1


texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
i = 0
max = len(texts) - 1
while i < max:
    print(i, texts[i], texts[i + 1])
    if len(texts[i]) == len(texts[i + 1]):
        print("\tFOUND!")
    i += 1

