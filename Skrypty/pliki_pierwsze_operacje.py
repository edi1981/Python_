f = open("D:/Users/pbutkowski/Desktop/AAAAA.txt", "w")
file = f.write("TEST")
# f.close()
f = open("D:/Users/pbutkowski/Desktop/AAAAA.txt", "r")
file = f.read()
f.close()

print(file)