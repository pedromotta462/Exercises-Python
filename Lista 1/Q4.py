salario = float(input("Diga quanto você ganha por hora(em reais): "))
horas = int(input("Diga o número de horas trabalhadas por mês: "))
bruto = salario * horas
impostodrenda = bruto * 0.11

inss = bruto * 0.08
sindicato = bruto * 0.05
descontos = impostodrenda + inss + sindicato
liquido = bruto - descontos

print("O seu salário bruto é: ", bruto, "reais")
print("Você pagou: ", inss, " reais ao INSS")
print("Você pagou: ", sindicato, " reais ao sindicato")
print("Seu salário líquido é: ", liquido, "reais")
print("No total foram descontados ", descontos, " reais do seu salário")