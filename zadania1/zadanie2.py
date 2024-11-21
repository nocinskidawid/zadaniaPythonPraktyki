from random import randint

lista = []
for i in range(20):
    lista.append(randint(1,10))
print("wylosowane liczby")
print(lista)
print("wystapienia:")

for i in range(1,11):
    print(str(i)+": "+ str(lista.count(i)))
