respostas = []
def decide(respostas):
    a = 0 #auxiliar
    b = 0 #quantidade de 's' respondidos
    #Contando quantos sim foram respondidos
    while a < len(respostas):
        if(respostas[a] == "a"):
            b += 1
        a += 1
    #dá o veredicto
    veredicto = {0: "Inocente", 1: "Inocente", 2: "Suspeita", 3: "Cúmplice", 4: "Cúmplice", 5: "Assassino"}
    return veredicto[b]

aux = " "
#pergunta 1
while (True):
    aux = str(input("Telefonou para a vítima? \n a)Sim b)Não \n:"))
    respostas.append(aux);
    if aux == "a" or aux == "b":
        break
    else:
        print("Resposta incorreta! Repetindo a pergunta...")
        respostas.pop(0)
        continue

#pergunta 2
aux = " "
while True:
    aux = str(input("Esteve no local do crime? \n a)Sim b)Não \n:"))
    respostas.append(aux);
    if aux == "a" or aux == "b":
        break
    else:
        print("Resposta incorreta! Repetindo a pergunta...")
        respostas.pop(1)
        continue
#pergunta 3
aux = " "
while aux != "a" or aux != "b":
    aux = str(input("Mora perto da vítima? \n a)Sim b)Não \n:"))
    respostas.append(aux);
    if aux == "a" or aux == "b":
        break
    else:
        print("Resposta incorreta! Repetindo a pergunta...")
        respostas.pop(2)
        continue
#pergunta 4
aux = " "
while aux != "a" or aux != "b":
    aux = str(input("Devia para a vítima? \n a)Sim b)Não \n:"))
    respostas.append(aux);
    if aux == "a" or aux == "b":
        break
    else:
        print("Resposta incorreta! Repetindo a pergunta...")
        respostas.pop(3)
        continue
#pergunta 5
aux = " "
while aux != "a" or aux != "b":
    aux = str(input("Já trabalhou com a vítima? \n a)Sim b)Não \n:"))
    respostas.append(aux);
    if aux == "a" or aux == "b":
        break
    else:
        print("Resposta incorreta! Repetindo a pergunta...")
        respostas.pop(4)
        continue

print(decide(respostas)) 