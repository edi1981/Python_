#################################################################
# zadanie ## chcemy z sumować 5 pierwszych nieparzystych liczb
#         ## opcje z WHILE i FOR
#################################################################

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
liczby_np = 0                           # ilość liczb nieparzystych
suma_np = 0                             # suma liczb nieparzystych
# i = 0                                 # wartość i używamy przy WHILE
dl_lst = len(num_list)                  # zapisujemy dł listy do zmiennej

# while (liczby_np < 5) and (i < dl_lst):
#    if num_list[i] % 2 != 0:
#        suma_np += num_list[i]
#        liczby_np += 1
#    i+=1
# print(suma_np)
# print(liczby_np)

for liczba in num_list:

    if (liczba % 2 != 0) and (liczby_np < 5):
        suma_np += liczba
        liczby_np += 1
print(suma_np)
print(liczby_np)

###################################################################################




# number = 6
# product = 1
# #b = 1
# # while temp <= a:
# #     b *= temp  # b = b * temp
# #     temp+=1
# #
# # print(b)
#
# for i in range(2, 7):
#     product *= i
# print(product)
