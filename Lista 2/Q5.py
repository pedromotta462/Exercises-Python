print("Digite 15 números:")
a = []
aux = 0
while aux < 15:
    a.append(int(input("Digite um número:")))
    aux += 1
print("Agora digite mais 15 números:")
b = []
aux = 0
while aux < 15:
    b.append(int(input("Digite um número:")))
    aux += 1
aux = 0
c = []
while aux < 15:
    c.append(a[aux])
    c.append(b[aux])
    aux += 1
print("tamanho das listas são:", len(a),", ", len(b), ", ", len(c))
print(a,",",b, "\n", c)