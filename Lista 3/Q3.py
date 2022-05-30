import time

palavrasecreta = str(input("Digite a palavra que será adivinhada: "))
palavra = list(palavrasecreta)
descobertas = []

acertou = False

print("-----------JOGO DA FORCA-----------")
iniciotempo = time.time() 
for i in range(0, len(palavra)):
    descobertas.append("_")
    print(descobertas[i])


tentativas = 7 #1 cabeça, 1 tronco, 2 braços, 2 pernas, 1 rosto(é o que tem num boneco palito de um jogo da forca normal)
while acertou == False:
    print("\nRestam: ", tentativas, "tentativas")   
    letra = str(input("Digite a letra que irá chutar: "))
    for i in range(0, len(palavra)):
        if letra == palavra[i]:
            descobertas[i] = letra
            tentativas += 1
        print(descobertas[i])
    tentativas -= 1        
    for x in range(0, len(descobertas)):
        if descobertas[x] == "_":
            acertou = False
    if descobertas == palavra:
        acertou = True
    if tentativas == 0:
        fimtempo = time.time() 
        print("\n---------Game Over!---------\n tempo de jogo:", fimtempo-iniciotempo)
        exit()

fimtempo = time.time() 
print("PARABÉNS VOCÊ ACERTOOOU!!!!\n tempo de jogo:", round(fimtempo-iniciotempo, 2), "segundos")