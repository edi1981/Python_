import random

word_file = "D:/Users/pbutkowski/Desktop/Programowanie/Python/Python/Pliki_txt/example_text.txt"
new_list = []   # służy nam do dodania wierszy z pliku jako list zagnieżdźonych
nowa_lista=[]   # lista zawierająca same wyrazy i znaki, poprzez odpowiednie podzielenie new_list

def remove_empty_lines():
    """Overwrite the file, removing empty lines and lines that contain only whitespace."""
    with open("D:/Users/pbutkowski/Desktop/Programowanie/Python/Python/Pliki_txt/example_text.txt", 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.writelines(line for line in lines if line.strip())
        f.truncate()
remove_empty_lines()

def generate_password():
    """funkcja losująca n słów z listy new_list """
    return random.choice(nowa_lista) + random.choice(nowa_lista) + random.choice(nowa_lista)


with open(word_file,'r') as wiersze:        # otwieramy plik jako wiersze
    for wiersz in wiersze:                  # wyciągamy poszczególne wiersze z pliku, każdy wiersz jest nested listą
        new_list.append(wiersz.split())     # do new_list dodajemy podlisty (wiersze)
for lista_main in new_list:                 # dobieramy się do list zagnieżdzonych w new_list
    for wyraz in lista_main:                # każdą nested listę dzielimy na wyrazy
        nowa_lista.append(wyraz)            # i dodajemy do nowej nowa_lista



print(generate_password())

