##############################################################
#                               FOR
##############################################################


tokens = ['<greeting>', 'Hello World!', '</greeting>']
xml = []
count = 0
for token in tokens:
    if token.startswith('<') and token.endswith('>'):
        xml.append(token)
        count += 1
print(xml)

print(count)




# names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
# usernames = []
#
# # write your for loop here
# for name in names:
#     name = name.replace(" ", "_").lower()
#     usernames.append(name)
#
# print(usernames)


# names = ["Ja", "Ty", "On", "Ona", "Ono", "My", "Wy", "Oni", "One"]
# domena = "gmail.com"
# for name in names:
#     email = name + "@" + domena
#     print("To email dla:\t" ,name, "\t", email)
# else:
#     print("\t\t----==== END ====----")



# data = ['Error:File cannot be open',
# #         'Error:No free space on disk',
# #         'Error:File missing',
# #         'Warning:Internet connection lost',
# #         'Error:Access denied']
# # for rekord in data:
# #     print(rekord.upper())




# data = ['Error:File cannot be open',
#         'Error:No free space on disk',
#         'Error:File missing',
#         'Warning:Internet connection lost',
#         'Error:Access denied']
# for rekord in data:
#     elements = rekord.split(":")
#     if elements[0] == "Error":
#         print(elements[0], elements[1].upper())
#     else:
#         print(elements[0], elements[1])

# string_A = '+---+---+---+---+'
# string_B = '|   |   |   |   |'
# for i in range(1,12):
#     if i %2 == 0:
#         print(string_B)
#     else:
#         print(string_A)


#for i in range(1,10):
#     if i %2 == 0:
#         print("x"*i)
#     else:
#         print("o"*i)


#
# for x in range(0,10):
#     for y in range(0,10):
#         print(x, "*", y, "=", x*y)


# list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
# list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']
#
# for noun in list_noun:
#     for adj in list_adj:
#         print(adj, noun)

# for kandydat in range(2,31):
#     for dzielnik in range(2, kandydat):
#         if kandydat % dzielnik == 0:
#             print("%2d nie jest liczbą pierwszą - dzielnikiem jest %2d" % (kandydat, dzielnik))
#             break
#     else:
#         print("%2d jest liczbą pierwszą" % kandydat)



