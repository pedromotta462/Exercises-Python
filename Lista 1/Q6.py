diasemana = str(input("Diga dia da semana em que você entrará de férias: "))
diames = int(input("Diga o dia do mês em que você entrará de férias: "))
ferias = int(input("Diga quantos dias você ficará de férias: "))

a = 0
semana = [' ', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo']

while a < 7:
    if diasemana in semana[a]:
        break
    a += 1

voltadiasemana = round((a + ferias)/7)
voltadiames = round((diames + ferias)%30) #considerando que todos os meses tenham 30 dias

print("Você entrou de férias no dia : ", diames, ",", diasemana, "- feira")
print("Depois de ",ferias, "dias de férias, você volta a trabalhar no dia: ", voltadiames, ",", semana[voltadiasemana], "- feira")