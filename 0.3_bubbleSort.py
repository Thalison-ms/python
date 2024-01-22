############# Fazer uso de PSEUDOCÓDICO
### - Bubble Sort
"""
    Para cada elemento i no array de tamanho n
        Para cada elemento j no array de tamanho n -1
            Se elemento i for maio que elemento j
                Troque os elementos i e j
    Exiba o array ordenado
"""

lista = [4, 3, 8, 1, 2, 5, 7, 0, 11, 61, 52, 32, 17, 20, 18, 41, 22]
tam = len(lista)
print(tam)
print("==========")

for i in range(tam):
    print("Tamanho: ", i)
    for j in range(0, tam-i-1):
        print(tam-i-1)
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
        
print(lista)
