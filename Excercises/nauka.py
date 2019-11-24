import string
spam = ["a", "b", "c", "d", "e"]

def lista(list):
    new_list = []
    final_list = []
    poczatek = list[:-1]
    koniec = list[-1:]


    for i in poczatek:
        new_list = ", ".join(poczatek)

    final_list.append(new_list)

    final_list.append(koniec)

    """
    Tu się zatrzymałem. Nie umiem połączyć elementów z listy w jeden string: "a,b,c,d i e"
    """




    # print(final_list[-1])
    #
    # print(final_list)


lista(spam)
