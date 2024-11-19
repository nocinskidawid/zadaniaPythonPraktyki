from random import randint

print("podaj a: ")
a = input()
print("podaj b: ")
b = input()
print("podaj n: ")
n = input()

macierz = []

for i in range(int(n)):
    macierz.append([])
    for j in range(int(n)):
        macierz[i].append(randint(int(a),int(b)))

print(macierz)

przekatna1 = 0
przekatna2 = 0
for i in range(int(n)):
    for j in range(int(n)):
        if i==j:
            przekatna1+=macierz[i][j]
        if i+j==int(n)-1:
            przekatna2+=macierz[i][j]
            #print(i,j)
        else:
            pass
sumaPrzekatych=przekatna1+przekatna2
print("suma przekatnych: "+str(sumaPrzekatych))


sumaNieparzystych = 0
for i in range(int(n)):
    if i%2!=0:
        for j in range(int(n)):
            if j%2!=0:
                sumaNieparzystych += macierz[i][j]
                #print(i,j)
            else:
                pass
    else:
        pass
print("suma nieparzystych: "+str(sumaNieparzystych))


for i in range(int(n)):
    macierz[i].reverse()

print(macierz)

