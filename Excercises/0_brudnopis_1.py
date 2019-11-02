# fibonacciIterations = 20
# a1 = 0
# a2 = 1
# a3 = 0
# for i in range(0,20):
#     print('Step',i,'value',a3)
#     a1=a2
#     a2=a3
#     a3=a1+a2

# teksts = """Industrial Light & Magic: In this case, you find Python
# used in the production process for scripting complex,
# computer graphic-intensive films. Originally, Industrial
# Light & Magic relied on Unix shell scripting, but it was
# found that this solution just couldn’t do the job. Python
# was compared to other languages, such as Tcl and Perl, and
# chosen because it’s an easier-to-learn language that the
# organization can implement incrementally. In addition, Python
# can be embedded within a larger software system as a scripting
# language, even if the system is written in a language such as
# C/C++. It turns out that Python can successfully interact with
# these other languages in situations in which some languages can’t."""
#
# lista = teksts.replace('\n', ' ').replace(',', '').replace('.', '').replace("'", "").split(' ')
# print(lista)
# i=0
# for slowoP in lista:
#      if slowoP.lower().find("p")>=0:    #if wykona blok kodu umieszczony za if,
#                                         # jeżeli warunek zwraca True. Dla uproszczenia
#                                         # życia programisów przyjęto, że jeśli wyrażenie
#                                         # w warunku if jest liczbą, to jak ta liczba jest <>0,
#                                         # to to jest True, a jak jest równa 0, to przyjmuje
#                                         # sie False
#         i+=1
#         print(slowoP)

# dictionary = {'A': '80%-10%', 'B': '60%-80%', 'C': '50-60%', 'D': 'less then 50%'}
# for word in dictionary.keys():
#     print(word, '-', dictionary[word])
#
#
#
#
#
# percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
#            2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
#            3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
#            4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
#            8.740978348,6.174819567]
# countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
#              'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
#              'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
#              'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
#              'Cyprus','Italy']
# sumOfPoints = 4988
# cou_len = len(countries)
# cou_per = len(percent)
# sum_percent = sum(percent)
#
# for i in range(len(countries)):
#     print(percent[i], int(percent[i]), round(percent[i], 2), int(round(percent[i] * sumOfPoints / 100, 0)),
#           countries[i])
