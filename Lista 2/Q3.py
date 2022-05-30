numeros = []
comparar = (1,2,3,4,5,6,7,8,9,10)
a=0
while a < 10:
    numeros.append(int(input("Digite um número de 1 a 10: ")))
    if numeros[a] not in comparar:
        print("Digitou um número que não está entre 1 e 10, então digite novamente...")
        numeros.pop(a)
        a -= 1
    a += 1
numerosdigitados = tuple(numeros)
print("\nVocê digitou: ", numerosdigitados)
print("O numero 5 foi digitado:", numerosdigitados.count(5), "vezes")
#vendo quantos 3 tem e quais suas posições
a=0
b=0 #vai contar quantos 3 tem na tupla
n3 = []
while a < len(numerosdigitados): 
    if(numerosdigitados[a] == 3):
        n3.append(a)
        b +=1
    a += 1
if b != 1:
    print("Os indices do número 3 são: ", n3)
else: print("o número 3 está na posição:", numerosdigitados.index(3))
#Vendo numeros pares e impares
impares = []
pares = []
a = 0
while a < len(numerosdigitados): 
    if (numerosdigitados[a]%2) == 0:
        pares.append(numerosdigitados[a])
    else:
        impares.append(numerosdigitados[a])
    a += 1
print("Numeros pares digitados:", pares)
print("Numeros ímpares digitados:", impares) 