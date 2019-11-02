# x = 0
# y = 1
#
# while y < 50:             #program polega na wyświetleniu sumy dwóch kolejnych liczb
#     print(x + y)          # z zakresu 0-50
#     x = y
#     y += 1

###########################################################

# import random
# myNumber = random.randint(0,20)
# guess = -1
# trials = 0                                           # Program pyta nas o liczbę, do póki nie
# print("Zgadnij liczbę!")                             # odgadnemy, którą wylosował z zakresu 0-20.
# while guess != myNumber:                             # Informuje nas, czy podaliśmy za niską,
#     guess = int(input())                             # czy za wysoką. Gdy zgadniemy, podaje
#     print("Zgadnij liczbę!", myNumber)               # liczbę prób, które wykonaliśmy.
#     trials += 1
#     if guess == myNumber:
#         print("Brawo! ", "Liczba prób:", trials)
#     elif guess > myNumber:
#      print("Twoja liczba jest większa niż kompa")
#     else:
#      print("Twoja liczba jest mniejsza niż kompa")

#######################################


# text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.'
# words = text.split(" ")
# print(words)
# short_text = ""
# counter = 0
# for word in words:
#     short_text += word + " "
#     counter+=1
#     if counter >= 5:
#         print(short_text)
#         break


# definitions = [
#     'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device or machine system. The device preserves the input power and simply trades off forces against movement to obtain a desired amplification in the output force. The model for this is the law of the lever. Machine components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism transmits power without adding to or subtracting from it. This means the ideal mechanism does not include a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear. The performance of a real system relative to this ideal.',
#     'Ein Kraftwandler ist eine mechanische Anordnung zur Veränderung einer Kraft in Bezug auf ihren Angriffspunkt, ihre Richtung oder ihren Betrag. Die einfachsten Kraftwandler sind Seile, Stangen, Rollen, schiefe Ebenen und Hebel. Dies sind gleichzeitig die grundlegenden einfachen Maschinen.',
#     'La ventaja mecánica es una magnitud adimensional que indica cuánto se amplifica la fuerza aplicada usando un mecanismo (ya sea una máquina simple, una herramienta o un dispositivo mecánico más complejo) para contrarrestar una carga de resistencia.',
#     'Cette notion s\'applique de manière évidente dans les systèmes de poulies et de leviers. Elle est centrale dans les systèmes de freinage : on applique une petite force sur un parcours important et l\'on obtient une force importante transmise au système de freinage pour une course de faible distance.'
# ]
#
# for definition in definitions:
#
#     words = definition.split(' ')
#     short_text = ''
#     counter = 0
#
#     for word in words:
#
#         short_text += word + ' '
#         counter += 1
#
#         if counter >= 5:
#             print(short_text)
#             break

# menu = '''
# Choose what you want me to do for you:
# 1 - COFFEE
# 2 - TEA
# 3 - MAKE ME SMILE
# ---------------
# To stop this script select 0
# '''
#
# smile = '''
#
#                           oooo$$$$$$$$$$$$oooo
#                       oo$$$$$$$$$$$$$$$$$$$$$$$$o
#                    oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
#    o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
# oo $ $ "$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
# "$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
#   $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
#   $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  """$$$
#    "$$$""""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$
#     $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     "$$$o
#    o$$"   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
#    $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" "$$$$$$ooooo$$$$o
#   o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
#   $$$$$$$$"$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$""""""""
#  """"       $$$$    "$$$$$$$$$$$$$$$$$$$$$$$$$$$$"      o$$$
#             "$$$o     """$$$$$$$$$$$$$$$$$$"$$"         $$$
#               $$$o          "$$""$$$$$$""""           o$$$
#                $$$$o                                o$$$"
#                 "$$$$o      o$$$$$$o"$$$$o        o$$$$
#                   "$$$$$oo     ""$$$$o$$$$$o   o$$$$""
#                      ""$$$$$oooo  "$$$o$$$$$$$$$"""
#                         ""$$$$$$$oo $$$$$$$$$$
#                                 """"$$$$$$$$$$$
#                                     $$$$$$$$$$$$
#                                      $$$$$$$$$$"
#                                       "$$$""""
# '''
#
# while True:
#
#     print(menu)
#     letter = input('Enter your choice  ')
#
#     if letter == '1':
#         print("Function COFFEE not implemented")
#         input('Press enter')
#         continue
#
#     if letter == '2':
#         print("Function TEA not implemented")
#         input('Press enter')
#         continue
#
#     if letter == '3':
#         print(smile)
#         input('Press enter')
#         continue
#
#     if letter == '0':
#         break
#
#     input('You need to make a valid choice. Press ENTER and try again!')


#
# initialCapital = 20000
# percent = 0.03
# maxTimeYears = 10
# year=0
# capital=initialCapital
# while year<maxTimeYears:
#     year+=1
#     capital=round((1+percent)*capital,2)
#     print('after this year:', year,  'you will have:',capital)
# else:
#     print('the total revenue is', capital-initialCapital)
# print('-------------------------------------------------------')


# number=20730906
#
# lnumber=list(str(number))       #polecenie list(str(number)) tworzy listę lnnumber
#                                 #która składa się z cyfr 2, 0, 7, 3..
# suma=0
#
# for t in lnumber:
#
#     suma+=int(t)
#
# print(suma)

# zdanie = """United Space Alliance: This company provides major support to NASA for
# various projects, such as the space shuttle. One of its projects is to
# create Workflow Automation System (WAS), an application designed to
# manage NASA and other third-party projects. The setup uses a central
# Oracle database as a repository for information. Python was chosen over
# languages such as Java and C++ because it provides dynamic typing and
# pseudo-code–like syntax and it has an interpreter. The result is that
# the application is developed faster, and unit testing each piece is easier."""

# zdanie_podzial = zdanie.split(" ")
#
# i=0
# szesc=[]
# for slowo in zdanie_podzial:
#     if len(slowo) >= 6:
#         szesc.append(slowo)
# print(len(szesc))


text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
listOfWords = text.replace('\n', ' ').replace(',', '').replace('.', '').split(' ')
wordLength = 6
i = 0
shortWords = 0
longWords = 0
while i < len(listOfWords):
    if len(listOfWords[i]) > wordLength:
        longWords += 1
    else:
        shortWords += 1

    i += 1
print("Words shorter than ", wordLength, ":", shortWords)
print("Words longer than ", wordLength, ":", longWords)
