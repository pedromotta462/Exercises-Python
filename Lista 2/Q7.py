idades = {}
def adicionarpessoas(idades):
    nome = str(input("diga o nome da pessoa: "))
    idades[nome] = (int(input("diga a idade dele: ")))

quantidade = int(input("Diga quantas pessoas você quer adicionar? "))
a=0
while a < quantidade:
    adicionarpessoas(idades)
    a+=1
print("Essas são todas as pessoas adicionadas e suas idades: \n", idades)
nomes = list(idades.values)
print(nomes)
ididis = []
idosos = []
jovens = []
a=0
while a < quantidade:
    ididis.append(idades[nomes[a]])
    if ididis[a] <= 30:
        jovens.append(nomes[a])
    else:
        idosos.append(nomes[a])
    a+=1
print("Aqui os idosos: \n", idosos)
print("Aqui os jovens: \n", jovens)