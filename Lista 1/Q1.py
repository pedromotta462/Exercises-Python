
dias = int(input("Diga quantos dias: "))
horas = int(input("Diga quantas horas: "))
minutos = int(input("Diga quantos minutos: "))
segundos = int(input("Diga quantos segundos: "))

if dias != 0 :
    dias *= 86400
if horas != 0:
    horas *= 3600
if minutos != 0:
    minutos *= 60

segundos += dias + horas + minutos

print("se passaram: ", segundos, " segundos")