####### DICIONÁRIO
import os
os.system('cls') 

dict1 = {'chave1': 1230, 'chave2': [22, 456, 73.4], 'chave3': ['picanha', 'fraldinha', 'alcatra']}
print(dict1)
print(dict1['chave2'])
print(dict1['chave3'])
for item in dict1['chave3']:
    print(item.upper())

print((dict1['chave1'] + 770))

# Dicionários Aninhados
print("-"*50)
dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em python'}}}
print(dict_aninhado)
print(dict_aninhado['key1']['key2_aninhada']['key3_aninhada'])
