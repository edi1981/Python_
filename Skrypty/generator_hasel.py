
# import random
#
# ints = range(33, 127)                                #budujemy tabelę znaków i cyfr
# password = ""                                        #hasło będzie napisem
# for i in range(16):                                  #hasło będzie miało 16 znaków
#     password += chr(random.choice(ints))             #do napisu doklejamy jedną z wartości tabeli ints
#
# print("Password: ", password)

import random

bLetters = range(65, 91)
sLetters = range(97, 123)
ints = range(48, 58)
sChars = range(33, 48)
password = []
dLitery = ""
mLitery = ""
liczby = ""
znaki = ""
nwPswd = ""

for i in range(4):
    for b in range(1):
        dLitery += chr(random.choice(bLetters))
        password.append(dLitery)
        for m in range(1):
            mLitery += chr(random.choice(sLetters))
            password.append(mLitery)
        for l in range(1):
            liczby += chr(random.choice(ints))
            password.append(liczby)
            for z in range(1):
                znaki += chr(random.choice(sChars))
                password.append(znaki)

password = [dLitery, znaki, mLitery, liczby]
random.shuffle(password)
nwPswd = ''.join(password)
input("Wciśnij ENTER aby wygenerować hasło")
print(nwPswd)
input("Wciśnij ENTER aby zamknąć okno")


