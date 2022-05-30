import random

numeros = []
numeros2 = [0,1,2,3,4,5,6,7,8,9,]
a=0
while a < 10:
    numeros.append(int(input("Digite um número de 0 a 9: ")))
    if numeros[a] not in numeros2:
        print("Digitou um número que não está entre 0 e 9, então digite novamente...")
        numeros.pop(a)
        a -= 1
    a += 1
random.shuffle(numeros)
random.shuffle(numeros2)

print("As dezenas sorteadas são: ")
a=0
while a<5:
    dezena1 = numeros[a]
    dezena2 = numeros2[a]
    a+=1
    if dezena1 == 0 and dezena2 == 0:
        random.shuffle(numeros)
        random.shuffle(numeros2)
    print(dezena1,",", dezena2)
