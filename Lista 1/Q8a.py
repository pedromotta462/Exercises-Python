npratos = int(input("Vamos fazer uma pilha de pratos! Diga quantos pratos terão na pilha, inicialmente: "))

pilha = []
a = 0
print("Para uma melhor vizualização, vamos nomear cada prato da pilha!")

while a < npratos:
    print("Diga o nome do ", a+1 ,"o prato")
    nome = str(input(": "))
    pilha.append(nome)
    a += 1

a = 0
print("Eis a sua pilha(em ordem crescente):")
while a < len(pilha):
    print(a+1, "o prato: ", pilha[a])
    a += 1

escolha2 = "n"
while escolha2 == "n":
    print("Gostaria de adicionar ou remover algum prato(digite 'a' ou 'b')? \n a)adicionar b)remover")
    escolha = str(input(": "))
    
    if escolha == "a":
        b = int(input("Diga em qual posição será colocado o prato na pilha: "))
        c = str(input("Diga em qual o nome do prato que será colocado na pilha: "))
        pilha.insert(b-1, c)

    a = 0
    if escolha == "b":
        while a < len(pilha):
            print(a+1, "o prato: ", pilha[a])
            a += 1
        remover = int(input("Digite qual posição do prato que voce quer remover: "))
        pilha.pop(remover-1)

    if escolha != "a" or escolha != "b":
        print("opção inválida")
    a = 0
    print("A pilha agora está desse jeito: ")
    while a < len(pilha):
        print(a+1, "o prato: ", pilha[a])
        a += 1
    escolha2 = str(input("Gostaria de encerrar o programa(digite 's' ou 'n')? \n s)Sim n)Não \n:"))
    
print("Encerrando...")