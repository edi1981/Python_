def create_cast_list(filename):
    """ Funkcja otwiera plik txt, pętla wyciąga linie tekstu z pliku, którą jest dzielona
    przez przecinek, następnie usuwany jest znak nowej linii przez line.rstrip("\n"),
    następnie elementy są dodawne do nowej listy cast_list"""
    cast_list = []
    with open("D:/Users/pbutkowski/Desktop/flying_circus_cast.txt") as f:
        for line in f:
            name = line.split(",")
            name = line.rstrip("\n")
            cast_list.append(name)

    return cast_list

    """ Wywołujemy funkcję, której argumentem, jest plik flying_circus_cast.txt """
cast_list = create_cast_list("D:/Users/pbutkowski/Desktop/flying_circus_cast.txt")
for actor in cast_list:
    print(actor)