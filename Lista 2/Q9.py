from tabulate import tabulate

produtos = (("abacate", "R$6.90"),("abacaxi", "R$9.30"),("beterraba", "R$3.70"),("melão","R$2.80"))

#Usando o módulo tabulate
print(tabulate(produtos, headers = ["Produtos", "Preços"]))

#Usando o .format
print ("\n\n{:<8} {:<15}".format('Produtos:','Preços:'))

for v in produtos:
    produtos, preços = v
    print ("{:<8} {:<15}".format( produtos, preços))