############# Fazer uso de PSEUDOCÓDICO
### - Calculadora Simples
"""
    Exiba "Bem-vindo à Calculadora"
    Peça para o usuário inserir o primeiro número
    Armazene o primeiro número em uma variável
    Peça para o usuário inserir o segundo número
    Armazene o segundo número em uma variável
    Peça para o usuário selecionar uma operação (+, -, *, /)
    Armazene a operação selecionada e os números aramazenados para realizar o cálculo
    Exiba o resultado
"""

print("Bem-vindo à Calculadora")
entrada1 = float(input("Insira o primeiro número: "))
entrada2 = float(input("Insira o segundo número: "))

print("Selecione uma das operações de acordo com o número da opção: \n1: +\n2: -\n3: *\n4: \\ \n0: Sair da aplicação")
operador = int(input())
cont = True
while(cont):
    if operador in [1, 2, 3, 4]:
        print("Realizando operação!......")

        if (entrada1 == 0 and operador == 4) or (entrada2 == 0 and operador == 4):
            print("Não é possível realizar a divisão por zero, finalizando a operação!")
            cont = False
            break

        if operador == 1:
            print(f" Resultado de {entrada1} + {entrada2} = ", entrada1 + entrada2)
            break
        elif operador == 2:
            print(f" Resultado de {entrada1} - {entrada2} = ", entrada1 - entrada2)
            break
        elif operador == 3:
            print(f" Resultado de {entrada1} * {entrada2} = ", entrada1 * entrada2)
            break
        elif operador == 4:
            print(f" Resultado de {entrada1} / {entrada2} = ", entrada1 / entrada2)
            break
        else:
            print("VAZIO") 
               
    elif operador == 0:
        print("Saindo da aplicação!......")
        break
    else:
        print("Valor informado não é válido! Finalizando aplicação....")
        break

print("\n\n\n")
