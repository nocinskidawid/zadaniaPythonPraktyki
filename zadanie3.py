from random import randint

macierz = [[],[],[],[],[]]

for i in range(len(macierz)):
    for j in range(5):
        macierz[i].append(randint(-5,5))

print(macierz)
#test gita
for i in range(len(macierz)):
    najmniejsza = min(macierz[i])
    najwieksza = max(macierz[i])
    print("min z kolumny "+str(i)+" = "+str(najmniejsza))
    print("max z kolumny "+str(i)+" = "+str(najwieksza))

