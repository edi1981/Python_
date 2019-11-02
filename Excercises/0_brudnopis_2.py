# import random
# #
# # min = 1
# # max = 6
# #
# # dice = random.randint(min, max)
# #
# # if dice == 1:
# #     print('   ')
# #     print(' o ')
# #     print('   ')
# # elif dice == 2:
# #     print('  o')
# #     print('   ')
# #     print('o  ')
# # elif dice == 3:
# #     print('  o')
# #     print(' o ')
# #     print('o  ')
# # elif dice == 4:
# #     print('o o')
# #     print('   ')
# #     print('o o')
# # elif dice == 5:
# #     print('o o')
# #     print(' o ')
# #     print('o o')
# # else:
# #     print('o o')
# #     print('o o')
# #     print('o o')
# #
# # print('----------------------')
# #
# # dices = []
# # for i in range(5):
# #     dices.append(random.randint(min, max))
# #
# # dices.sort()
# # print(dices)

import string

poem = '''1.Runą i w łunach spłoną pożarnych 
Krzyże kościołów, krzyże ofiarne 
I w bezpowrotnym zgubi się szlaku 
W lechickiej ziemi Orzeł Polaków. 
2.O, jasne słońce- wodzu Stalinie! 
Niech sława twoja nigdy nie zginie 
Niechaj jak orły powiedzie z gniazda 
Rosja i z Kremla płonąca gwiazda. 
3.Na ziemskim globie flagi czerwone 
Będą na wiatrach grały jak dzwony 
Czerwona Armia i wódz jej Stalin 
Odwiecznych wrogów na zawsze obali! 
4.Zaćmisz się rychło w czarnej godzinie 
Polsko- Twe córy i syny, 
Wiara i każdy krzyż na mogile, 
U stóp am legą w prochu i pyle! '''

lines = poem.split("\n")
print(lines)
for i in range(8):
    print(lines[i])
    print(lines[i+8])