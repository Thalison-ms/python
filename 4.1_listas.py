####### LISTAS / DICIONÁRIO / TUPLA
import os
os.system('cls') 

print("-"*50)
lista_1 = ["arroz, frango, tomate, leite"]                  # Criando lista com somente 1 STRING
print(lista_1)
print(type(lista_1))

print("-"*50)
lista_2 = ["laranja", "cebola", "banana", "alho"]           # Criando lista com várias STRINGS
print(lista_2)
print(type(lista_2))

print("-"*50)
lista_3 = [23, 100, "Cientista de Dados"]                   # Criando lista mista
print(lista_3)
print(type(lista_3))


print("-"*50)
# Atribuindo valores da lista a variáveis
item1 = lista_2[0]
item2 = lista_2[3]
print(item1, item2)

# Atualizar item da lista
lista_3[0] = "chocolate"
print(lista_3)

# Deletando item da lista
del lista_3[2]
print(lista_3)

# Listas de listas (listas aninhadas)
print("-"*50)
listas = [[1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]]
print(listas)
print(listas[0])
print(listas[2])
print(listas[2][1])
print(listas[0] + listas[1] + listas[2])

