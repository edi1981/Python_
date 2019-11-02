line = "very STRANGE text it IS"

print(line.capitalize())            # capitalize porządkuje zdanie i ustawia pierwszą wielką literę w zdaniu
print(line.title())                 # title ustawia na wielką każdą pierwszą literę wyrazu w zdaniu
print(line.swapcase())              # zamienia każdą małą literkę na dużą i odwrotnie
print(line.count('e'))              # liczy ilość wystąpień litery
print(line.find('e'))               # pokazuje numer pozycji pierwszego wysapienia litery e od lewej
print(line.rfind('e'))              # pokazuje numer pozycji pierwszego wysapienia litery e od prawej
# """ """                           # """ dłuuuuuugi tekst w wielu liniach """

import string                       # dzieki temu mamy dodatkowe opcje do działania z tekstem
a = string.digits                   # 0123456789
b = string.punctuation              # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
c = string.printable                # 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(c)


tekst = "AAA bbb CCC 222"
tekst2 = tekst.split(' ')           # dzielimy teks na listę rozbijając go o spacje (' ')
                                    # lista = tekst.split(' ') - możemy wrzucić do zmiennej
print(tekst2)

tekst3 = ' '.join(tekst2)           # łączymy elementy tabeli w tekst izapiujemy je w zmiennej
print(tekst3)
