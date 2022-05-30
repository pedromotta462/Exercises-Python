from calendar import c


a = {'pera','banana'}
b = {'arroz', 'feijao'}
ingredientes = [a , b]
c = []
print("Vamos criar uma receita com conjuntos de ingredientes!\n")
a = 0
while a == 0:
    print('O que você quer fazer?')
    escolha = str(input("a)Ver conjuntos de ingredientes disponíveis \n b)Criar conjunto de ingredientes \n c)Juntar ingredientes \n d)Juntar todos os ingredientes"))
    if escolha == 'a':
        for n in range(len(ingredientes)):
            print('\n', ingredientes[n])
    if escolha == 'b':
        n = int(input('Quantos ingredientes este conjunto terá?'))
        aux = 0
        while(aux < n):
            c[n] = str(input('Digite o nome do ingrediente: '))
        set(c)      
    if escolha == 'c':
        print('a')
    if escolha == 'd':
        print('b')
    if escolha != 'a' or escolha != 'b' or escolha != 'c' or escolha != 'd':
        print('Escolha indisponível!')