####### OPERADORES / TIPOS DE DADOS

import os
os.system('cls') 

"""
    +   Soma
    -   Subtração
    *   Multiplicação
    /   Divisão
    **  Potência
    %   Módulo
"""
print("-"*50)
print("TYPE")
a = "teste"
print(type(1))
print(4+4.0)
print(4//2)
print(4/2)

print("-"*50)
print("ORDEM DE OPERADORES")
# 1 - () Parenteses
# 2 - ** Potência
# 3 - * Multiplicação
# 4 - / Divisão
# 5 - // Módulo
# 6 - % Porcentagem
# 7 - + e - Soma e subtração
# A soma entra strings gera a concatenação

print("-"*50)
print("CONVERSAO")
a = 6
b = float(a)
print(a)
print(b)

print("-"*50)
print("FUNCOES ABS, ROUND, POW")
print(abs(-8))                      # Transforma um número negativo em positivo
print(round(3.141416,2))            # Arredonda com número de casas desejado
print(pow(4,2))                     # Realiza a potência, número/potência
