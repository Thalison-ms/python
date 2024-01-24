####### LISTAS Funções Built-in
import os
os.system('cls') 

lista_numeros = [10, 20, 50, -3.4]
print(len(lista_numeros))
print(max(lista_numeros))
print(min(lista_numeros))

print("-"*50)
lista1 = ['A', 'B', 'B', 'João']
print(lista1)
lista1.append("Macarrão")
print(lista1)
print(lista1.count('B'))


# Criando lista vazia
a = []

print("-"*50)
# Copiando itens de uma lista para outra
old_list = [1, 3, 5, 7, 10]
print(old_list)
new_list = []

for item in old_list:
    new_list.append(item)
print(new_list)

print("-"*50)
# Adiciona os valores de uma lista X a outra lista Y
cidades = ['Recife', 'Manaus', 'Salvador']
print(cidades)
cidades.extend(['Fortaleza', 'Palmas'])
print(cidades)
# Verifica qual o indíce da palavra dentro da lista
print(cidades.index('Salvador'))
# Insere uma informação em determinada posição da lista
cidades.insert(2, 110)
print(cidades)
# Remove um item da lista
cidades.remove('Palmas')
print(cidades)


# Ordenar lista
old_list.sort()
print(old_list)
# Reverter lista
old_list.reverse()
print(old_list)
