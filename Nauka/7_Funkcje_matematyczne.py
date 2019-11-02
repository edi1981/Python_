# import math
#
# degree = 45
# radian = degree * math.pi / 180
# print("%d degree is %f radians" % (degree, radian))
# print('')
#
# print("%d degree is %f radians" % (360, math.radians(360)))
# print("%d degree is %f radians" % (45, math.radians(45)))
# print('')



#
# import random
# aaa=[]                                                      # losujemy 10 liczb z zakresu 1-100
# for i in range(10):                                         # i wrzuca je pustej tablicy
#     random.randint(1, 100)
#     aaa.append(random.randint(1, 100))
# print(aaa)

# do zmiennej number1 wylosuj liczbę całkowitą z zakresu 1-100
# twoim celem będzie losowanie liczb losowych tak długo,
# aż znowu wylosujesz liczbę number1.
# Dodatkowo chcemy policzyć ile prób jest do tego potrzebnych
# # do zmiennej counter zapisz 1
# # do zmiennej number2 wylosuj liczbę z zakresu 1-100
# # wyświetl numer próby (counter) i wylosowaną liczbę (number2)
# # Tak długo jak długo number1 jest inne niż number2
# # zwiększ counter o 1
# # wylosuj ponownie liczbę number2 (liczba całkowita od 1 do 100)
# # wyświetl numer próby (counter) i wylosowaną liczbę (number2)
# # Na zakończenie wyświetl podsumowanie z infromacją o ilości prób

# import random
# counter = 0
# i = random.randint(1,100)
# for n in range(1,100):
#     n = random.randint(1,100)     #w moim rozwiązaniu max liczba prób to 99, potem się
#                                   #program się wywala
#     if n != i:
#         counter+=1
#         continue
#     else:
#         break
#
# print(i)
# print(n)
# print(counter)

# import random
# number1 = random.randint(1, 100)
# print("The first generated number is %d" % (number1))
#
# counter = 1
# number2 = random.randint(1, 100)
#
# while number1 != number2:
#     counter += 1
#     number2 = random.randint(1, 100)
#     print(counter, number2)
#
# print("I needed %d attempts to generate %d again" % (counter, number1))

import random
countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]
random.shuffle(countries)

groupNumber = 0
for i in range(len(countries)):
    if i % 4 == 0:
        groupNumber += 1
        print("========== Group %d ==========" % (groupNumber))
    print(countries[i])