####### STRINGS E FUNÇÕES BUILT-IN
import os
os.system('cls') 

s = "seja bem vindo ao universo de Linguagem Python"

print("-"*50)
print(s)
print(s.upper())            # Deixa tudo maiusculo
print(s.lower())            # Deixa tudo minusculo
print(s.split())            # Por padrão converte para lista separando por espaço
print(s.split('y'))         # Porém é possível separar por alguma informação
print(s.capitalize())       # Primeira letra fica maiuscula
print(s.count('a'))         # Conta o total de itens passado no parênteres
print(s.isalnum())          # Verifica se é numérico
print(s.islower())          # Verifica se está tudo minusculo
print(s.isspace())          # Verifica se a string tem só espaço
print(s.endswith('o'))      # Verifica se a string termina com a letra 'o'



