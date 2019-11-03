tekst =[]
final_list=[]
aaa=[]
nf = open("D:/Users/pbutkowski/Desktop/Programowanie/Python/Python/Pliki_txt/new_file.txt", "r")
lines = nf.readlines()
lines.remove("\n")
for element in lines:
    final_list.append(element.strip().split())

print(final_list)
print(final_list[0])









# nf2 = open("D:/Users/pbutkowski/Desktop/Programowanie/Python/Python/Pliki_txt/text.txt", "w")
# nf2.writelines(tekst)
# print(tekst)
# nf2.close()





