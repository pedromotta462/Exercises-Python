print("Há uma lista com todos os números primos de 1 ate 200!")
x = int(input("Digite quantos números primos quer encontrar nessa lista?"))
primos = []
a = 1
while len(primos) < x:
    if a%1 == 0 and a%a == 0:
        primos.append(a)
    if a%2 == 0 or a%3 == 0 or a%5 == 0 or a%7 == 0 or a%11 == 0:
        primos.remove(a)
    if a == 200:
        break
    a += 1
    
primos.remove(1)
if x == 1 or x > 1:
     primos.insert(0, 2)
if x == 2 or x > 2:
    primos.insert(1, 3)
if x == 3 or x > 3:
    primos.insert(2, 5)
if x == 4 or x > 4:
    primos.insert(3, 7)
if x == 5 or x > 5:
    primos.insert(4, 11)

print("Eis os seus números primos: ", primos) 