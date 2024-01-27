####### DICIONÁRIO
import os
os.system('cls') 


lista_estudates1 = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25]    # Lista normal
print(type(lista_estudates1))
lista_estudates2 = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}
print(type(lista_estudates2))
print(lista_estudates2)
print(lista_estudates2["Ana"])

print("-"*50)
lista_estudates2["Marcelo"] = 23                # Cria nova chave dentro do dicionário
print(lista_estudates2)
print(lista_estudates2["Marcelo"])

print("-"*50)
lista_estudates2.clear()
print(lista_estudates2)
lista_estudates2 = {1: "Cavalo", 2: "Porco", 3:"Bezerro"}
del lista_estudates2
#print(lista_estudates2)

print("-"*50)
lista_estudates2 = {"nome": "José", "idade": 27, "cpf": 5895789, "cidade": "Tangará" }
print(lista_estudates2)
print(len(lista_estudates2))
print(lista_estudates2.keys())
print(lista_estudates2.values())
print(lista_estudates2.items())

print("-"*50)
estudantes = {"maria": 27, "gilberto": 30, "mireli": 45}
lista_estudates2.update(estudantes)
print(lista_estudates2)
lista_estudates2["mireli"] = 50
print(lista_estudates2)
lista_estudates2["Thalison"] = 28
print(lista_estudates2)
