import math

print("podaj n: ")
n = input()

macierz = []

for i in range(int(n)):
    macierz.append([])
    for j in range(int(n)):
        if math.gcd(i+1,j+1)==1:
            macierz[i].append("+")
        else:
            macierz[i].append(".")

for i in macierz:
    print(" ".join(i))