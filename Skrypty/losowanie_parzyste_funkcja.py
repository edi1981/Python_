zbior = []
for i in range(0,101):
    if i%2==0:
        zbior.append(i)
print(zbior)


def parzyste(a,b):
    """ pętla pobiera argument a, sprawdza, czy jest parzysty, jeśli nie dodając 1 uzykujemy
    parzystość, b jest ostatnim elementem zbioru, 2 to krok, o który porusza się pętla """
    for parzysta in range(a+1 if a%2 else a,b,2):
        print(parzysta)
parzyste(101, 204)