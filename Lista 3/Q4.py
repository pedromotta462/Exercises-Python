import random
import sys

tabuleiro = [ [" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "] ]

vitoria = [ [0,0,0],
         [0,0,0],
         [0,0,0] ]

def jogadado():
    dado = random.randrange(1,4)
    return dado

def decidequemcomeça(d1,d2):
    if(d1 < d2):
        print("O jogador 2 irá começar!")
        return 2
    if(d1 > d2):
        print("O jogador 1 irá começar!")
        return 1
    if(d1 == d2):
        print("Os dados deram iguais... Joguem os dados novamente!")
        return 0

def tabuleirojogodavelha():               
    print("      0    1    2")
    print("0:  ", tabuleiro[0][0]," | ", tabuleiro[0][1], " | ", tabuleiro[0][2] )
    print("    ---------------")
    print("1:  ", tabuleiro[1][0]," | ", tabuleiro[1][1], " | ", tabuleiro[1][2] )
    print("    ---------------")
    print("2:  ", tabuleiro[2][0]," | ", tabuleiro[2][1], " | ", tabuleiro[2][2] )

def jogo(jogador):
    print()
    if jogador == 1:
        tabuleirojogodavelha()
        print("Jodador: ", jogador, "está jogando...")
        try:    
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))     
            if tabuleiro[linha][coluna] != " ":
                print("Está casa já está ocupada, tente novamente.")
                jogo()        
            tabuleiro[linha][coluna] = 'X'
            vitoria[linha][coluna] = 1
            w = win()
            if w == 1:
                print("temos um vencedoooor!! O jogador: ", jogador ,"Venceu!!!")
                sys.exit()
            else:
                jogador = 2   
                jogo(jogador)
        except:
            print("linha ou coluna inválida, tente novamente.")
            jogo(jogador)

    if jogador == 2:
        tabuleirojogodavelha()
        print("Jodador: ", jogador, "está jogando...")
        try:    
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))     
            if tabuleiro[linha][coluna] != " ":
                print("Está casa já está ocupada, tente novamente.")
                jogo()        
            tabuleiro[linha][coluna] = 'O'
            vitoria[linha][coluna] = -1
            w = win()
            if w == 1:
                print("temos um vencedoooor!! O jogador: ", jogador ,"Venceu!!!")
            else:
                jogador = 1   
                jogo(jogador)  
        except:
            print("linha ou coluna inválida, tente novamente.")
            jogo(jogador)


def win():
    #checando linhas
    for i in range(3):
        soma = vitoria[i][0]+vitoria[i][1]+vitoria[i][2]
        if soma==3 or soma ==-3:
            return 1

     #checando colunas
    for i in range(3):
        soma = vitoria[0][i]+vitoria[1][i]+vitoria[2][i]
        if soma==3 or soma ==-3:
            return 1

    #checando diagonais
    diagona1 = vitoria[0][0]+vitoria[1][1]+vitoria[2][2]
    diagona2 = vitoria[0][2]+vitoria[1][1]+vitoria[2][0]
    if diagona1==3 or diagona1==-3 or diagona2==3 or diagona2==-3:
        return 1

    return 0

print("\n------------JOGO DA VELHA------------")
print("Primeiro vamos decidir qual jogador irá começar! O maior dado vence!")
jogador1 = 0
while jogador1 == 0:
    dado1= jogadado()
    print("- O primeiro jogador jogou o dado... o dado parou no número: ", dado1)
    dado2= jogadado()
    print("- Agora o segundo jogador jogou o dado... o dado parou no número: ", dado2)
    jogador1 = decidequemcomeça(dado1, dado2)

jogo(jogador1)