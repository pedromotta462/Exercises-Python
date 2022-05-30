import modulomatematico as mat

def MDC(a, b): #algoritimo de euclides
    if (b == 0):
        return a
    else:
        return MDC(b, a % b)

def menu():
    escolha = int(input("\nDigite oq gostaria de calcular:\n 0)Calculo de área \n 1)Calculo de volume \n 2)MDC \n 3)Sair do programa \n:")) 
    
    if escolha == 0 or escolha == 1 or escolha == 2 or escolha == 3:        
        if escolha == 0:
            a = int(input("\nDigite o comprimento: "))
            b = int(input("Digite a largura: "))
            area = mat.mult(a,b)
            print("A área é: ", area)
            menu()
        if escolha == 1:
            c = int(input("\nDigite o comprimento: "))
            d = int(input("Digite a largura: "))
            e = int(input("Digite a altura: "))
            volume = mat.mult(mat.mult(c,d),e)
            print("o volume é: ", volume)
            menu()
        if escolha == 2:
            f = int(input("Digite o primeiro número: ")) 
            g = int(input("Digite o primeiro número: ")) 
            mdc = MDC(f, g)
            print("O MDC entre eles é: ", mdc)       
            menu()     
        if escolha == 3:
            print("Saindo...")
    else:
        print("Opção inválida! Por favor, digite uma opção válida.")
        menu()

menu()

