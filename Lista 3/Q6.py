'''Incompleta'''

contatos = []

def menu():
    print("--------------Menu:--------------")
    print("1 - Inserir")
    print("2 - Atualizar")
    print("3 - Pesquisar")
    print("4 - Apagar")
    escolha1 = int(input("Escolha uma opção:"))

    if (escolha1 == 1):
        inserir()
    if (escolha1 == 2):
        atualizar()
    if (escolha1 == 3):
        pesquisar()
    if (escolha1 == 4):
        apagar()


def inserir():
    
    nome = str(input("\nDigite o nome do contato que deseja adicionar: "))
    telefone = str(input("\nDigite o número do contato: "))
    email = str(input("\nDigite o seu email: "))
    arquivo = open("Q6.txt", "r", encoding="utf-8") 
    
    a = arquivo.read()
    print("\n", a)
    arquivo.close()
    
def atualizar():
    b=0
def apagar():
    c=0
def pesquisar(): 
    d=0

menu()