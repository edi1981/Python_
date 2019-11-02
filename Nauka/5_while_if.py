cargo = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 14, 15, 17, 20, 21, 23, 23, 34, 50, 32, 34, 54, 67, 57, 90, 14, 11, 1, 3, 5]
cargo.sort()
cargo.reverse()
print(cargo)
boxCapacity = 100
box = []

i = 0


#while sum(box) + cargo[i] <= boxCapacity and i < len(cargo):
while i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)):
    if (boxCapacity - sum(box) >= cargo[i]):
        box.append(cargo[i])
    i += 1
    boxDiff = boxCapacity - sum(box)

print("Pozostało jeszcze", boxDiff)
print("Suma boxa:", sum(box))
print("Elementy boxa to:", box)




