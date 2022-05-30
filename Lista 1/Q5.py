salario = float(input("Diga o seu salário(em reais): "))
aumento = int(input("Diga o aumento no salario(em pocentagem): "))

reajuste = salario * (aumento/100)
novosalario = salario + reajuste

print("O seu salário aumentou em: ", round(reajuste, 2), "reais")
print("O seu salário agora é: ", round(novosalario, 2), "reais")