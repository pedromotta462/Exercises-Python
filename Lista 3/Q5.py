arquivo = open('Q5.txt', encoding="utf-8")
saída = open("saida_paginada.txt", "w", encoding="utf-8") #O encoding ="utf-8" é para poder pegar normalmente os carateres especiais e acentos
maxCaracteres = 76
maxLinhas = 60

def verificapag(arquivo, linha, pag): #função que vai verificar se esta na ultima linha
    if linha == maxLinhas:  #se estiver na linha 60(ultima linha)
        textolinhafinal = f" Q6.txt - pag: {pag} " #o 'f' antes das "" é para que seja possivel adicionar uma variável no meio do texto
        arquivo.write(textolinhafinal.center(maxCaracteres - 1) + "\n") #escreve o texto na linha final da página
        pag += 1   #ajusta o valor do nº da proxima pagina
        linha = 1 #reseta a contagem das linhas
    return linha, pag 


def escreve(arquivo, linha, nlinhas, pag): #função que irá escrever no arquivo cada linha
    arquivo.write(linha + "\n") 
    return verificapag(arquivo, nlinhas + 1, pag)

pag = 1
linhas = 1

for linha in arquivo.readlines(): #lendo cara linha do arquivo
    palavras = linha.split(" ") #Separa as palavras de cada linha de acordo com os " " espaços
    linha = "" #"zera" o valor da string
    for p in palavras: #ira percorrer todas as palavras da linha
        p = p.strip() #remove os espaços em branco no inicio e no fim, deixando apenas a palavra
        if len(linha) + len(p) + 1 > maxCaracteres: #quebrando a linha em 76 caracteres
            linhas, pag = escreve(saída, linha, linhas, pag) 
            linha = ""
        linha += p + " " #readicionando as palavras e os espaçoes da linha
    if linha != "": #quando não há mais linhas, completa o arquivo com "" até a ultima linha da página atual 
        linhas, pag = escreve(saída, linha, linhas, pag) #implementando o arquivo de saida de acordo com os parametros de 76 caracteres na linha e 60 linhas

# Para imprimir o número na última página
while(linhas != 1):
    linhas, pag = escreve(saída, "", linhas, pag) #implementando o arquivo de saida
#Fechamento dos arquivos
arquivo.close() 
saída.close()