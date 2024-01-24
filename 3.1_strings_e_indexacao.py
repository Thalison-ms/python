####### STRINGS E INDEXAÇÃO
import os
os.system('cls') 


# Dados do tipo texto
variavel1 = "Oi"
variavel2 = 'Criando uma string com aspas simples'
variavel3 = "Teste com aspas duplas e 'aspas simples'"

print('Testando \n Strings \n  em \n   Python')        # Quebra de linha

# Indexação SIMPLES
print("-"*50)
s = 'Data Science Academy'
print(s[0])
print(s[3])
print(s[5])
print(s[10])

# Indexação com dois pontos :
print("-"*50)
print(s[:5])
print(s[6:8])
print(s[8:])

# Indexação de trás para frente
print("-"*50)
print(s[-3])
print(s[-14:-10])
print(s[:-5])

# Indexação Fatiada
print("-"*50)
print(s[::2])
print(s[::5])
print(s[::1])       # Padrão

