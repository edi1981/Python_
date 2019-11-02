#####################################################################################
#                               LISTY
#####################################################################################

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
num = [10,23,3,54,51,16,28,9]


q3 = numbers[:2]
print(q3)
print(len(numbers))

print(max(numbers))     # w zależności co zawiera lista: jeśli to są liczby, dostajemy największą,
                        # jeśli są to stringi to dostajemy ostatni el jeśli posortowalibyśmy
                        # alfabetycznie

print(min(numbers))     # analogicznie jak MAX, tyle, że w drugą stronę

############################################################################################

print(sorted(num))                  # sortujemy liczby od min do max
print(sorted(num, reverse=True))    # sortujemy liczby od max do min

############################################################################################

print("\n".join(numbers))   # .join tworzy listę w oparciu o separator, który podamy przed .join

############################################################################################

numbers.append("AAA")       # dodawanie elementów do listy
print(numbers)              # --------





#for liczby in numbers:                 #
#    liczba = liczby.split(',')         # dzielenie listy
#    print(liczba)                      #


############################################################################################
#                           SET
############################################################################################
num_num = [10,23,3,54,51,16,28,9,0,10,23,16,9]      #
num_set = set(num_num)                              # SET służy do tworzenia czegoś w rodzaju listy
print(num_set)                                      # tzw SETu, który nie posiada powtarzających się
                                                    # wartości. SET jest nieuporządkowany i nie posiada
                                                    # ostatniego elementu

num_set.add(100)                                    # dodawanie el do SETa
print(num_set)

num_set.pop()                                       # POP usuwa randomowy element z SETa
print(num_set)



############################################################################################

#############################
# funkcja list zip
#############################
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))   # output [('a', 1), ('b', 2), ('c', 3)]

letters = ['a', 'b', 'c']
nums = [1, 2, 3]
some_list = [('a', 1), ('b', 2), ('c', 3)]     #
letters, nums = zip(*some_list)                # output ('a', 'b', 'c') (1, 2, 3)
print(letters, nums)                           #

########### Tworzenie koordynat z 4 list  ##############
# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
#
# points = []
# for point in zip(labels, x_coord, y_coord, z_coord):
#     points.append("{}: {}, {}, {}".format(*point))
#
# for point in points:
#     print(point)
##########################################################


##############################
# funkcja list enumerate
#############################

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

#output
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e

##############################################################################################
#                                   TUPLES
##############################################################################################
location = (13.4125, 103.866667)        # tuple przechowują stałe, niezmienne wartości
                                        # np. dł i szer geograf.