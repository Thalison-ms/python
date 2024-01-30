####### TUPLAS
import os
os.system('cls') 

# Tuplas são imutáveis

tupla1 = ("Geografia", 23, "Eleafantes", 9.8, 'Python')
print(tupla1)
# tupla1.append("Chocolate") # Não é possível alterar ou inserir informações de Tuplas
print(tupla1)
del tupla1
# print(tupla1)
tupla1 = ("Chocolate", 50)
print(tupla1)
print(tupla1[0])
print(tupla1[1])
# tupla1[0] = 10 # Não é possível mudar dados atráves de indíces

# Converter Tupla para lista
lista = list(tupla1)
lista.append("Thalison")
print(lista)
tupla1 = tuple(lista)
print(tupla1)
