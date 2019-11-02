# INSTRUKCJE "IF"

min_like = 500
min_share = 10
#if min_like >=500 and min_share >=100:
#    print("Rabat 10%")
#else:
#    print("Ni mo rabatu")

if min_like < 500:
    print("Ni mo lajków")
elif min_share < 100:
    print("Ni mo szeróf !!! Ni mo rabata !!!")
else:
    print("Masz rabata!!!!!!!!!!")


# INSTRUKCJE "IF ELIF ELSE"
age = 18
isDrunk = False
isForbidden = False

if age < 18:
    print("Jesteś za młody żeby kupić alkohol")
elif isDrunk:
    print("Osobom pijanym nie sprzedajemy")
elif isForbidden:
    print("Zakaz sprzedarzy w tym miejscu")
else:
    print("Ile browarów podać?")
