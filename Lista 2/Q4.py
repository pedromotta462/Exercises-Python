carros = ["fusca", "gol", "hb20", "polo", "etios", "sandero", "celta", "uno", "nivus", "corolla"]
consumo = [10.7, 13.3, 13.9, 12.9, 16.6, 13.2, 13.8, 13.4, 10.7, 12.3]
modeloeconomico = consumo.index(max(consumo))
print("O modelo mais econômico é o:", carros[modeloeconomico])
x = round(float(input("Digite um número X km percorridos:")), 3)
a = 0
print("O consumo e dinheiro gasto com combustível de cada carro em ", x, "km percorridos é:")
while a < len(consumo):
    preço = (x/consumo[a])*5.50
    print(carros[a], ": ", round(x/consumo[a], 3), "L, gastando:R$",
    round(preço, 2))
    a += 1
