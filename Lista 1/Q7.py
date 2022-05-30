str1 = str(input("Digite uma palavra: "))
str2 = str(input("Digite outra palavra: "))

print("Você digitou primeiro: ", str1, "que tem ", len(str1), "digitos" )
print("Depois você digitou: ", str2, "que tem ", len(str2), "digitos" )

if len(str1) is len(str2):
    print("As duas palavras tem o mesmo número de dígitos")
if str1 in str2:
    print("Você digitou a mesma coisa")