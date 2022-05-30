npessoas = int(input("Vamos organizar uma fila de um banco! Diga quantas pessoas terão na fila, inicialmente: "))

fila = []
a = 0
print("Para uma melhor vizualização, vamos nomear cada pessoa da fila!")

while a < npessoas:
    print("Diga o nome da ", a+1 ,"o pessoa")
    nome = str(input(": "))
    fila.append(nome)
    a += 1

a = 0
print("Eis a sua fila:")
while a < len(fila):
    print(a+1, "o pessoa: ", fila[a])
    a += 1

escolha2 = "n"
while escolha2 == "n":
    print("Gostaria de adicionar ou remover algum pessoa(digite 'a' ou 'b')? \n a)adicionar b)remover")
    escolha = str(input(": "))

    if escolha == "a":
        b = int(input("Diga em qual posição será colocado a pessoa na fila: "))
        c = str(input("Diga em qual o nome do pessoa que será colocado na fila: "))
        fila.insert(b-1, c)
    
    a = 0

    if escolha == "b":
        while a < len(fila):
            print(a+1, "o pessoa: ", fila[a])
            a += 1
        remover = int(input("Digite qual posição da pessoa que voce quer remover: "))
        fila.pop(remover-1)

    if escolha != "a" or escolha != "b":
        print("opção inválida")
    a = 0
    print("A fila agora está desse jeito: ")
    while a < len(fila):
        print(a+1, "o prato: ", fila[a])
        a += 1
    
    escolha2 = str(input("Gostaria de encerrar o programa(digite 's' ou 'n')? \n s)Sim n)Não \n:"))
print("Encerrando...")