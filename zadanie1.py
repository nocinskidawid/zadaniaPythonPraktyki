from random import randint

lista = []
for i in range(10):
    lista.append(randint(-10,10))
print("wylosowane liczby")
print(lista)

minEl = min(lista)
maxEl = max(lista)
print("min: "+str(minEl)+"max: "+str(maxEl))

srednia = sum(lista)/len(lista)
print("srednia: "+str(srednia))

mniejsze = 0
wieksze = 0

for i in range(len(lista)):
    if lista[i] < srednia:
        mniejsze+=1
    elif lista[i] > srednia:
        wieksze+=1

print("wiekszych od sredniej: "+str(wieksze))
print("mniejszych od sredniej: "+str(mniejsze))

print("liczby w odwrotnej kolejnosci")
listaOdworcona = []
for i in range(len(lista)+1):
    if i == 0:
        pass
    else:
        print(lista[-i])
        #listaOdworcona.append(lista[-1])
#print(listaOdworcona)
