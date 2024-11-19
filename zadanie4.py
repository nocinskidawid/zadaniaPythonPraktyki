import math

print("podaj a: ")
a = input()
print("podaj b: ")
b = input()

#print(a,b)

lista = []
for i in range(int(a),int(b)):
    if i%2!=0:
        wartosc = i
        dwaDoPotegi = math.pow(2,wartosc)
        pierwiastek = math.sqrt(wartosc)
        lista.append((wartosc, dwaDoPotegi, pierwiastek))
    else:
        pass

print(lista)