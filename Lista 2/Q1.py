valorcasa = float(input("Digite o valor da casa que será comprada: "))
salario = float(input("Digite o valor do seu salário: "))
anos = float(input("Digite a quantidade de anos a pagar: "))
prestacao = round(valorcasa/(anos*12), 2)
if prestacao > round(salario*0.3, 2):
    print("Impréstimo não aprovado, o valor da prestação é maior que 30% do seu salário.")
else:
    print("Seu impréstimo foi aprovado.") 