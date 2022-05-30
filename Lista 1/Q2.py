nome = str(input("Diga seu nome: "))
salario = float(input("Diga seu salário(em reais): "))
if salario > 1200:
    print("Pague os impostos! ", nome)
else:
    print(nome, "Você não paga impostos!")